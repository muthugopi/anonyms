from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    list_display = ('email', 'register_number', 'department', 'graduation_year', 'is_verified', 'role', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_verified', 'role', 'groups')
    ordering = ('email',)
    search_fields = ('email', 'register_number')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'register_number', 'department', 'graduation_year')}),
        ('Status', {'fields': ('is_verified', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'is_verified', 'role'),
        }),
    )
