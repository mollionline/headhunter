from django.urls import path
from headhunter.views.resume_views import ResumeCreateView, ResumeDetailView


urlpatterns = []

resume_urls = [
    path('resume/create', ResumeCreateView.as_view(), name='create_resume'),
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='detail_resume')
]

urlpatterns += resume_urls

from django.urls import path

from headhunter.views import vacancy_views

urlpatterns = []

vacancy_urls = [
    path('vacancy/list/', vacancy_views.VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', vacancy_views.VacancyDetailsView.as_view(), name='vacancy_details'),
    path('vacancy/create/', vacancy_views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:pk>/', vacancy_views.VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy/delete/<int:pk>/', vacancy_views.VacancyDeleteView.as_view(), name='vacancy_delete'),
]

urlpatterns += vacancy_urls

