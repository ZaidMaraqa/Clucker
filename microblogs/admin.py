"""Configuration of the adminstrative interface for microblogs."""
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configurationof the admin interface for user"""
    list_display = [
        'username', 'first_name', 'last_name', 'email', 'is_active',
    ]
