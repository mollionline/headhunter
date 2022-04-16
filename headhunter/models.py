from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.fields import related
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
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='resume_user', verbose_name='Пользователь'
    )
    name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(null=True, max_length=150, verbose_name='Фамилия')
    position = models.CharField(max_length=200, verbose_name='Должность')
    category = models.CharField(max_length=100, choices=CATEGORIES, verbose_name='Категория')
    salary = models.IntegerField(
        null=True, validators=[MaxValueValidator(1000000), MinValueValidator(1)],
        verbose_name='Заработная плата'
    )
    phone_number = PhoneNumberField(region='KZ', verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    telegram = models.URLField(max_length=500, verbose_name='Telegram')
    facebook = models.URLField(max_length=500, null=True, blank=True, verbose_name='Facebook')
    linkedin = models.URLField(max_length=500, null=True, blank=True, verbose_name='Linkedin')
    work_experience = models.ManyToManyField('headhunter.Experiences', related_name='resume_experience', blank=True)
    education = models.ManyToManyField('headhunter.Educations', related_name='resume_education', blank=True)
    publication = models.BooleanField(default=False, verbose_name='Публикация резюме')
    about_me = models.TextField(max_length=2000, null=True, verbose_name='Об о мне')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.position}'


class Vacancy(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='vacancy_user')
    position = models.CharField(max_length=100, null=False, blank=False, verbose_name='Должность')
    category = models.CharField(max_length=100, choices=CATEGORIES, verbose_name='Категория')
    salary = models.IntegerField(null=False, blank=False, verbose_name='Заработная плата')
    description = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Описание вакансии')
    min_years_experience = models.IntegerField(null=False, blank=False, verbose_name='Мин кол-во лет опыта')
    max_years_experience = models.IntegerField(null=False, blank=False, verbose_name='Макс кол-во лет опыта')
    posted_status = models.BooleanField(null=False, blank=False, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата обновления')


class Respond(models.Model):
    vacancy_applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='vacancy_applicant')
    employer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='employer')
    resume = models.ForeignKey('headhunter.Resume', on_delete=models.CASCADE, related_name='respond_resume')
    vacancy = models.ForeignKey('headhunter.Vacancy', on_delete=models.CASCADE, related_name='respond_vacancy')


class RespondMessage(models.Model):
    respond = models.ForeignKey('headhunter.Respond', on_delete=models.CASCADE, related_name='respond_message')
    message = models.ForeignKey('headhunter.Message', on_delete=models.CASCADE, related_name='message_text')


class Message(models.Model):
    applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='applicant')
    text = models.CharField(max_length=3000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
