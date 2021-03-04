from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('user-config/', views.user_config_list, name="user-config-list"),
    path('user-config/<int:pk>', views.user_config_detail, name="user-config-detail"),
    path('user-config/<str:username>', views.username_config_detail, name="username_config_detail"),
    path('user-config/create/', views.user_config_create, name="user-config-create"),
    path('register/', views.registration_view, name="register"),
    path('login/', obtain_auth_token, name="login"),
]