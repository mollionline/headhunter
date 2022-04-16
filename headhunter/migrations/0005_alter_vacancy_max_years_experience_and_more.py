# Generated by Django 4.0.3 on 2022-04-16 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headhunter', '0004_rename_user_vacancy_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='max_years_experience',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)], verbose_name='Макс кол-во лет опыта'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='min_years_experience',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)], verbose_name='Мин кол-во лет опыта'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3000000), django.core.validators.MinValueValidator(1)], verbose_name='Заработная плата'),
        ),
    ]