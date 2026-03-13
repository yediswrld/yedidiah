from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'price_amount', 'price_currency', 'pay_currency', 'status', 'created_at')
    list_filter = ('status', 'pay_currency')
    search_fields = ('user__email', 'nowpayments_id')
    readonly_fields = ('nowpayments_id', 'pay_address', 'pay_amount', 'created_at', 'updated_at')
    ordering = ('-created_at',)
