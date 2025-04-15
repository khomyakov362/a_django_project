import string
from random import sample

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib import messages
from django.views.generic import CreateView, UpdateView

from users.models import User
from users.forms import UserRegisterForm, UserLoginForm, UserForm, UserUpdateForm, UserChangePasswordForm
from users.services import send_register_email, send_new_password


def user_register(request : HttpRequest):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            send_register_email(new_user.email)
            return HttpResponseRedirect(reverse('users:user_login'))
    context = {
        'title' : 'Create new account',
        'form' : form
    }
    return render(request, 'users/user_register.html', context=context)

def user_login(request : HttpRequest):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is None:
                return HttpResponse('No such account exists.')
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dogs:index'))
            else:
                return HttpResponse('The account is inactive.')
    context = {
        'title' : 'Sign In',
        'form'  : UserLoginForm
    }
    return render(request, 'users/user_login.html', context=context)

@login_required
def user_profile(request : HttpRequest):
    user_object = request.user
    if user_object.first_name:
        user_name = user_object.first_name + " " + user_object.last_name
    else:
        user_name = 'Anonymous'
    context = {
        'title' : f'Your profile {user_name}'

    }
    return render(request, 'users/user_profile_read_only.html', context)

@login_required
def user_update(request : HttpRequest):
    user_object = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user_object)
        if form.is_valid():
            user_object.save()
            return HttpResponseRedirect(reverse('users:user_profile'))
    context = {
        'object' : user_object,
        'title' : f'Change profile {user_object.first_name + " " + user_object.last_name}',
        'form' : UserUpdateForm(instance=user_object)
    }
    return render(request, 'users/user_update.html', context)

def user_logout(request : HttpRequest):
    logout(request)
    return redirect('dogs:index')

@login_required
def change_user_password(request : HttpRequest):
    user_object = request.user
    form = UserChangePasswordForm(user_object, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user_object = form.save()
            update_session_auth_hash(request, user_object)
            messages.success(request, 'The password has been successfully changed.')
            return HttpResponseRedirect(reverse('users:user_profile'))
        else:
            messages.error(request, 'The password could not be changed.')
    context = {
        'form' : form,
    }
    return render(request, 'users/user_change_password.html', context)

@login_required
def user_generate_new_password(request : HttpRequest):
    new_password = ''.join(sample(string.ascii_letters + string.digits, 12))
    request.user.set_password(new_password)
    request.user.save()
    send_new_password(request.user.email, new_password)
    return redirect(reverse('dogs:index'))

