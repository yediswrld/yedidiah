from django.db import models
from django.conf import settings


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('waiting', 'Waiting'),
        ('confirming', 'Confirming'),
        ('confirmed', 'Confirmed'),
        ('finished', 'Finished'),
        ('failed', 'Failed'),
        ('expired', 'Expired'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nowpayments_id = models.CharField(max_length=100, unique=True)
    pay_address = models.CharField(max_length=200, blank=True)
    pay_amount = models.DecimalField(max_digits=20, decimal_places=8, null=True, blank=True)
    pay_currency = models.CharField(max_length=20, blank=True)
    price_amount = models.DecimalField(max_digits=10, decimal_places=2)
    price_currency = models.CharField(max_length=10, default='USD')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.email} — ${self.price_amount} — {self.status}'
