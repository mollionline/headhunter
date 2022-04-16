from django.urls import path
from headhunter.views.resume_views import ResumeCreateView, ResumeDetailView


urlpatterns = []

resume_urls = [
    path('resume/create', ResumeCreateView.as_view(), name='create_resume'),
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='detail_resume')
]

urlpatterns += resume_urls
