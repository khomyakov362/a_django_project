from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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
        'object_list' : Dog.objects.filter(breed_id=pk),
        'title' : f'Dogs of {breed_item.name} breed',
        'breed_pk' : breed_item.pk
    }
    return render(request, 'dogs/dogs.html', context)

class DogListView(ListView):
    model = Dog
    extra_context = {
        'title' : 'Shelter - All Our Dogs'
    }
    template_name = 'dogs/dogs.html' 

class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogForm
    template_name = 'dogs/create_update.html'
    extra_context = {
        'title' : 'Add a new dog'
    }
    success_url = reverse_lazy('dogs:dogs_list')
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class DogDetailView(LoginRequiredMixin, DetailView):
    model = Dog
    template_name = 'dogs/detail.html'
    extra_context = {
        'title' : 'Details'
    }

class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    form_class = DogForm
    template_name = 'dogs/create_update.html'
    extra_context = {
        'title' : 'Edit information about the dog'
    }

    def get_success_url(self):
        return reverse('dogs:dog_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset = None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

class DogDeleteView(LoginRequiredMixin, DeleteView):
    model = Dog
    template_name = 'dogs/delete.html'
    extra_context = {
        'title' : 'Delete dog'
    }
    success_url = reverse_lazy('dogs:dogs_list')

    def get_object(self, queryset = None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object
    
