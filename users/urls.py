from django.urls import path
from users.apps import UsersConfig
from users import views

app_name = UsersConfig.name

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('', views.user_login, name='user_login')
]