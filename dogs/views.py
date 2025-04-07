from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from dogs.models import Breed, Dog
from dogs.forms import DogForm

def index(request : HttpRequest):
    context = {
        'objects_list' : Breed.objects.all()[:3],
        'title' : 'Shelter - Main'
    }

    return render(request, 'dogs/index.html', context)

def breeds_list(request : HttpRequest):
    context = {
        'objects_list' : Breed.objects.all(),
        'title' : 'Shelter - All Our Breeds'
    }
    return render(request, 'dogs/breeds.html', context)

def breed_dogs_list(request : HttpRequest, pk : int):
    breed_item = Breed.objects.get(pk=pk)
    context = {
        'objects_list' : Dog.objects.filter(breed_id=pk),
        'title' : f'Dogs of {breed_item.name} breed',
        'breed_pk' : breed_item.pk
    }
    return render(request, 'dogs/dogs.html', context)

def dogs_list(request : HttpRequest):
    context = {
        'objects_list' : Dog.objects.all(),
        'title' : 'Shelter - All Our Dogs'
    }
    return render(request, 'dogs/dogs.html', context)

@login_required
def dog_create(request : HttpRequest):
    form = DogForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            dog_object = form.save(commit=False)
            dog_object.owner = request.user
            dog_object.save()
            return HttpResponseRedirect(reverse('dogs:dogs_list'))
    return render(request, 'dogs/create_update.html', {'form':DogForm})

def dog_view_details(request : HttpRequest, pk : int):
    dog_object = Dog.objects.get(pk=pk)
    context = {
        'object' : Dog.objects.get(pk=pk),
        'title'  : f'You chose {dog_object.name}.\nBreed: {dog_object.breed.name}.' 
    }
    return render(request, 'dogs/detail.html', context=context)

@login_required
def dog_update(request : HttpRequest, pk : int):
    dog_object = get_object_or_404(Dog, pk=pk)
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dog_object)
        if form.is_valid():
            dog_object = form.save()
            dog_object.save()
            return HttpResponseRedirect(reverse('dogs:dog_detail', args={pk : pk}))
    context = {
        'object' : dog_object, 
        'form'   : DogForm(instance=dog_object)
    }
    return render(request, 'dogs/create_update.html', context)

@login_required
def dog_delete(request : HttpRequest, pk : int):
    dog_object = get_object_or_404(Dog, pk=pk)
    if request.method == 'POST':
        dog_object.delete()
        return HttpResponseRedirect(reverse('dogs:dogs_list'))
    context = {
        'object' : dog_object
    }
    return render(request, 'dogs/delete.html', context)

