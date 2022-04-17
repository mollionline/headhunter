from django import forms

from headhunter.models import Resume, Experiences, Educations


class ResumeForm(forms.ModelForm):
    about_me = forms.CharField(required=False)
    salary = forms.IntegerField(required=False)

    class Meta:
        model = Resume
        exclude = ['user']


class ResumeUpdateForm(forms.ModelForm):
    about_me = forms.CharField(required=False)
    salary = forms.IntegerField(required=False)

    class Meta:
        model = Resume
        exclude = ['user', 'work_experience', 'education']


class ExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Experiences
        fields = ['name_company', 'start_date', 'end_date', 'position', 'responsibilities']


class EducationUpdateForm(forms.ModelForm):
    class Meta:
        model = Educations
        fields = ['institution_name', 'start_date', 'end_date', 'speciality']
