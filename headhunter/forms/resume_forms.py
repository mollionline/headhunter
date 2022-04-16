from django import forms

from headhunter.models import Resume


class ResumeForm(forms.ModelForm):
    about_me = forms.TimeField(required=False)
    salary = forms.IntegerField(required=False)

    class Meta:
        model = Resume
        exclude = ['user']
