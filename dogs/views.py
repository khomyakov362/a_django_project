from django.shortcuts import render

from dogs.models import Breed, Dog

def index(request):
    context = {
        'objects_list' : Breed.objects.all()[:3],
        'title' : 'Shelter - Main'
    }

    return render(request, 'dogs/index.html', context)
