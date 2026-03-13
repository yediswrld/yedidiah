from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'read', 'created_at')
    list_filter = ('read',)
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)

    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = 'Mark selected as read'
