import string
from random import sample

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib import messages
from django.views.generic import CreateView, UpdateView

from users.models import User
from users.forms import UserRegisterForm, UserLoginForm, UserForm, UserUpdateForm, UserPasswordChangeForm
from users.services import send_register_email, send_new_password

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user_login')
    template_name = 'users/user_register.html'
    extra_context = {
        'title' : 'User registration'
    }

class UserLoginView(LoginView):
    template_name = 'users/user_login.html' 
    form_class = UserLoginForm
    extra_context = {
        'title' : 'Sign in'
    }

class UserProfileView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_profile_read_only.html'
    extra_context = {
        'title' : 'Your Profile'
    }

    def get_object(self, queryset = None):
        return self.request.user

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:user_profile')
    extra_context = {
        'title' : 'Update Profile'
    }

    def get_object(self, queryset = None):
        return self.request.user

class UserLogoutView(LogoutView):
    pass

class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/user_change_password.html'
    success_url = reverse_lazy('users:user_profile')

@login_required
def user_generate_new_password(request : HttpRequest):
    new_password = ''.join(sample(string.ascii_letters + string.digits, 12))
    request.user.set_password(new_password)
    request.user.save()
    send_new_password(request.user.email, new_password)
    return redirect(reverse('dogs:index'))

