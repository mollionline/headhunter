from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


CATEGORIES = [
    ('Medicine', 'Медицина'),
    ('Production', 'Производство'),
    ('Information technology', 'Информационные технологий'),
    ('Marketing', 'Маркетинг'),
    ('Sales', 'Продажи'),
    ('Other', 'Другое')
]


class Experiences(models.Model):
    name_company = models.CharField(max_length=1000, null=False, verbose_name='Имя компаний')
    start_date = models.DateField(null=False, blank=True, verbose_name='Дата начало')
    end_date = models.DateField(null=False, blank=True, verbose_name='Дата конца')
    position = models.CharField(max_length=500, null=False, verbose_name='Должность')
    responsibilities = models.TextField(max_length=2000, null=True, verbose_name='Обязанности')

    def __str__(self):
        return f'{self.name_company}: {self.start_date}-{self.end_date}'


class Educations(models.Model):
    institution_name = models.CharField(max_length=1000, null=False, verbose_name='Название учереждения')
    start_date = models.DateField(null=False, blank=True, verbose_name='Дата начало')
    end_date = models.DateField(null=False, blank=True, verbose_name='Дата конца')
    speciality = models.CharField(max_length=500, null=False, verbose_name='Специальность')

    def __str__(self):
        return f'{self.institution_name}: {self.start_date}-{self.end_date}'


class Resume(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default='1', related_name='resume_user')
    name = models.CharField(max_length=200, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=200, null=False, verbose_name='Фамилия')
    email = models.EmailField(max_length=300, null=False, verbose_name='Почта')
    position = models.CharField(max_length=500, null=False, verbose_name='Должность')
    salary = models.CharField(max_length=500, null=True, verbose_name='Желаемая зарплата')
    telegram = models.CharField(max_length=300, null=True, verbose_name='Телеграмм')
    facebook = models.CharField(max_length=300, null=True, verbose_name='Facebook')
    category = models.CharField(max_length=100, choices=CATEGORIES, verbose_name='Категорий')
    phone = PhoneNumberField(blank=False, verbose_name='Номер телефона', region='KZ', null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='resume_pics', verbose_name='Фото')
    experience = models.ManyToManyField('headhunter.Experiences', related_name='resume', blank=True)
    education = models.ManyToManyField('headhunter.Educations', related_name='resum', blank=True)
    about_me = models.TextField(max_length=5000, null=True, verbose_name='О себе')

    def __str__(self):
        return f'{self.position}'
