# Generated by Django 4.0.3 on 2022-04-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headhunter', '0007_merge_20220416_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='resumes',
            field=models.ManyToManyField(blank=True, related_name='vacancy_resume', to='headhunter.resume'),
        ),
    ]