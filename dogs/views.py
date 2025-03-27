from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

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
        'objects' : Dog.objects.all(),
        'title' : 'Shelter - All Our Dogs'
    }
    return render(request, 'dogs/dogs.html', context)

def dog_create(request : HttpRequest):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dogs:dogs_list'))
    return render(request, 'dogs/create.html', {'form':DogForm()})