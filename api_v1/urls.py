from django.urls import include, path
from api_v1.views import LogoutView, ExperienceCreateView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),
    path('experience/create/', ExperienceCreateView.as_view(), name='experience_create')
]
