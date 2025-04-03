from django.urls import path
from dogs import views
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('breeds/', views.breeds_list, name='breeds'),
    path('breeds/<int:pk>/dogs/', views.breed_dogs_list, name='breed_dogs'),
    path('dogs/', views.dogs_list, name='dogs_list'),
    path('dogs/create_update/', views.dog_create, name='dog_create'),
    path('dogs/detail/<int:pk>/', views.dog_view_details, name='dog_detail'),
    path('dogs/create_update/<int:pk>/', views.dog_update, name='dog_update'),
    path('dogs/delete/<int:pk>/', views.dog_delete, name='dog_delete')
]

