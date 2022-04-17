from django.urls import path

from headhunter.views import vacancy_views
from headhunter.views.resume_views import (
    ResumeCreateView, ResumeDetailView, ResumeDeleteView, ResumeUpdateView,
    ExperienceUpdateView, ExperienceDeleteView, EducationUpdateView, EducationDeleteView,
    ExperienceCreateView, EducationCreateView
)

urlpatterns = []

vacancy_urls = [
    path('', vacancy_views.VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', vacancy_views.VacancyDetailsView.as_view(), name='vacancy_details'),
    path('vacancy/create/', vacancy_views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/<int:pk>/update', vacancy_views.VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy/delete/<int:pk>/', vacancy_views.VacancyDeleteView.as_view(), name='vacancy_delete'),
]

urlpatterns += vacancy_urls

resume_urls = [
    path('resume/create/', ResumeCreateView.as_view(), name='create_resume'),
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='detail_resume'),
    path('resume/delete/<int:pk>/', ResumeDeleteView.as_view(), name='delete_resume'),
    path('resume/update/<int:pk>/', ResumeUpdateView.as_view(), name='update_resume'),
    path('experience/update/<int:pk>/<int:resume>/', ExperienceUpdateView.as_view(), name='update_experience'),
    path('experience/delete/<int:pk>/<int:resume>/', ExperienceDeleteView.as_view(), name='delete_experience'),
    path('education/update/<int:pk>/<int:resume>/', EducationUpdateView.as_view(), name='update_education'),
    path('education/delete/<int:pk>/<int:resume>/', EducationDeleteView.as_view(), name='delete_education'),
    path('experience/create/<int:pk>/', ExperienceCreateView.as_view(), name='experience_create'),
    path('education/create/<int:pk>/', EducationCreateView.as_view(), name='create_education')
]

urlpatterns += resume_urls
