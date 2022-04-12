from django.urls import path

from headhunter.views import vacancy_views

urlpatterns = []

vacancy_urls = [
    path('vacancy/list/', vacancy_views.VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', vacancy_views.VacancyDetailsView.as_view(), name='vacancy_details'),
    path('vacancy/create/', vacancy_views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:pk>/', vacancy_views.VacancyCreateView.as_view(), name='vacancy_update'),
    path('vacancy/delete/<int:pk>/', vacancy_views.VacancyDeleteView.as_view(), name='vacancy_delete'),
]

urlpatterns += vacancy_urls

