from django.urls import path
from users.apps import UsersConfig
from users import views

app_name = UsersConfig.name

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('profile', views.user_profile, name='user_profile'),
    path('update/', views.user_update, name='user_update'),
    path('change_password/', views.change_user_password, name='user_change_password'),
    path('profile/genpassword/', views.user_generate_new_password, name='user_generate_new_password')
]