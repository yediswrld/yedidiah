from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'email', 'country', 'trading_experience', 'why_join', 'instagram', 'telegram', 'discord']
        widgets = {
            'trading_experience': forms.Textarea(attrs={'rows': 4}),
            'why_join': forms.Textarea(attrs={'rows': 4}),
        }


def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            if request.user.is_authenticated:
                application.user = request.user
            application.save()

            # Notify admin
            send_mail(
                subject=f'New Mentorship Application — {application.full_name}',
                message=f'New application from {application.full_name} ({application.email}).\n\nCheck the admin panel to review.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True,
            )

            messages.success(request, 'Application submitted! We will review and get back to you.')
            return redirect('apply_success')
    else:
        form = ApplicationForm()
    return render(request, 'mentorship/apply.html', {'form': form})


def apply_success(request):
    return render(request, 'mentorship/apply_success.html')
