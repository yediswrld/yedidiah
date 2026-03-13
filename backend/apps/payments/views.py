import hashlib
import hmac
import json
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Payment


NOWPAYMENTS_BASE = 'https://api.nowpayments.io/v1'


def _headers():
    return {'x-api-key': settings.NOWPAYMENTS_API_KEY, 'Content-Type': 'application/json'}


@login_required
def create_payment(request):
    """Create a NOWPayments invoice and redirect user to payment page."""
    if request.method == 'POST':
        amount = request.POST.get('amount', '0')
        currency = request.POST.get('currency', 'btc')

        payload = {
            'price_amount': float(amount),
            'price_currency': 'usd',
            'pay_currency': currency,
            'order_description': 'Yedidiah Mentorship',
            'success_url': settings.NOWPAYMENTS_SUCCESS_URL,
            'cancel_url': settings.NOWPAYMENTS_CANCEL_URL,
            'ipn_callback_url': request.build_absolute_uri('/payments/ipn/'),
        }

        try:
            resp = requests.post(f'{NOWPAYMENTS_BASE}/invoice', json=payload, headers=_headers(), timeout=10)
            data = resp.json()

            if resp.status_code == 200 and 'id' in data:
                Payment.objects.create(
                    user=request.user,
                    nowpayments_id=data['id'],
                    price_amount=amount,
                    price_currency='USD',
                    status='pending',
                )
                return redirect(data['invoice_url'])
            else:
                return render(request, 'payments/error.html', {'error': data.get('message', 'Payment creation failed.')})

        except requests.RequestException:
            return render(request, 'payments/error.html', {'error': 'Could not connect to payment provider. Try again.'})

    return render(request, 'payments/checkout.html')


@csrf_exempt
@require_POST
def ipn_callback(request):
    """Handle NOWPayments IPN (Instant Payment Notification)."""
    sig = request.headers.get('x-nowpayments-sig', '')
    body = request.body

    # Verify signature
    secret = settings.NOWPAYMENTS_IPN_SECRET.encode()
    expected = hmac.new(secret, body, hashlib.sha512).hexdigest()
    if not hmac.compare_digest(sig, expected):
        return HttpResponse(status=400)

    data = json.loads(body)
    payment_id = str(data.get('payment_id', ''))
    status = data.get('payment_status', '')

    try:
        payment = Payment.objects.get(nowpayments_id=payment_id)
        payment.status = status
        payment.save()

        if status == 'finished':
            user = payment.user
            user.mentorship_active = True
            user.is_student = True
            user.save()

    except Payment.DoesNotExist:
        pass

    return HttpResponse(status=200)


@login_required
def payment_success(request):
    return render(request, 'payments/success.html')
