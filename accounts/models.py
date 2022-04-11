from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    email = models.EmailField(blank=False, null=False, unique=True)
    phone = PhoneNumberField(blank=False, verbose_name='Номер телефона', region='KZ', unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    user_or_company = models.BooleanField(null=False, blank=False, verbose_name='Соискатель', default=False)

    def __str__(self):
        return f"{self.user.get_full_name()}'s Profile"
