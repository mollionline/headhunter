from rest_framework import serializers
from headhunter.models import Experiences


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiences
        fields = ['id', 'name_company', 'start_date', 'end_date', 'position', 'responsibilities']

