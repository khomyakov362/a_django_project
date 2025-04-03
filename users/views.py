from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from users.forms import UserRegisterForm, UserLoginForm

def user_register(request : HttpRequest):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('dogs:index'))
    context = {
        'title' : 'Create new account',
        'form' : UserRegisterForm
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
