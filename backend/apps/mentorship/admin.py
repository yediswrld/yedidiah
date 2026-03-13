from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'country', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('full_name', 'email', 'country')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Applicant', {'fields': ('user', 'full_name', 'email', 'country')}),
        ('Application', {'fields': ('trading_experience', 'why_join')}),
        ('Socials', {'fields': ('instagram', 'telegram', 'discord')}),
        ('Review', {'fields': ('status', 'admin_notes')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )

    actions = ['approve_applications', 'reject_applications', 'mark_awaiting_payment']

    def approve_applications(self, request, queryset):
        queryset.update(status='approved')
    approve_applications.short_description = 'Approve selected applications'

    def reject_applications(self, request, queryset):
        queryset.update(status='rejected')
    reject_applications.short_description = 'Reject selected applications'

    def mark_awaiting_payment(self, request, queryset):
        queryset.update(status='awaiting_payment')
    mark_awaiting_payment.short_description = 'Mark as awaiting payment'
