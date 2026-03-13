from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'full_name', 'is_student', 'mentorship_active', 'date_joined')
    list_filter = ('is_student', 'mentorship_active', 'is_staff')
    search_fields = ('email', 'full_name', 'discord_username')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Mentorship', {'fields': ('is_student', 'mentorship_active', 'mentorship_start', 'discord_username', 'telegram_username', 'notes')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )
