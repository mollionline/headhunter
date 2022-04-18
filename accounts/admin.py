from django.contrib import admin
from accounts.models import Profile
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['user', 'email', 'phone', 'avatar', 'user_or_company']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]


User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
