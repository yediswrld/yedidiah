from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.mentorship.models import Application
from apps.payments.models import Payment


@login_required
def dashboard(request):
    user = request.user
    application = Application.objects.filter(user=user).last()
    payments = Payment.objects.filter(user=user).order_by('-created_at')
    context = {
        'user': user,
        'application': application,
        'payments': payments,
    }
    return render(request, 'dashboard/index.html', context)
