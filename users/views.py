from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserRegisterForm

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