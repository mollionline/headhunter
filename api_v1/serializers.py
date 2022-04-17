from rest_framework import serializers
from headhunter.models import Experiences, Educations


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiences
        fields = ['id', 'name_company', 'start_date', 'end_date', 'position', 'responsibilities']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educations
        fields = ['id', 'institution_name', 'start_date', 'end_date', 'speciality']
