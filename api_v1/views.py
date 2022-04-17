from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api_v1.serializers import ExperienceSerializer, EducationSerializer
from headhunter.models import Vacancy, Resume


class LogoutView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class ExperienceCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class EducationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class AddResumeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, pk=request.data['vacancy'])
        resume = get_object_or_404(Resume, pk=request.data['resume'])
        for resum in vacancy.resumes.all():
            if resum.pk == int(request.data['resume']):
                return Response({'error': 'Вы уже откликнулись'}, status=400)
        vacancy.resumes.add(resume)
        return Response({'answer': 'Откликнулись'})
