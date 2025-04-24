from django.urls import path
from users.apps import UsersConfig
from users import views

app_name = UsersConfig.name

urlpatterns = [
    # account management
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('update/', views.UserUpdateView.as_view(), name='user_update'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name='user_change_password'),
    path('profile/genpassword/', views.user_generate_new_password, name='user_generate_new_password'),
    # looking at other users
    path('all_users/', views.UserListView.as_view(), name='user_list')
]