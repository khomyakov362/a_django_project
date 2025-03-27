from django.urls import path
from dogs.views import index, breeds_list, breed_dogs_list, dogs_list, dog_create
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('breeds/', breeds_list, name='breeds'),
    path('breeds/<int:pk>/dogs/', breed_dogs_list, name='breed_dogs'),
    path('dogs/', dogs_list, name='dogs_list'),
    path('dogs/create/', dog_create, name='dog_create')
]

