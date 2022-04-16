from django import forms

from headhunter.models import Vacancy


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ['position', 'salary', 'category', 'description', 'min_years_experience',
                  'max_years_experience', 'posted_status']
