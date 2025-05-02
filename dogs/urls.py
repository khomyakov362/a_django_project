from django.urls import path
from dogs import views
from dogs.apps import DogsConfig
from django.views.decorators.cache import cache_page, never_cache

app_name = DogsConfig.name

urlpatterns = [
    path('', cache_page(60)(views.index), name='index'),
    path('breeds/', cache_page(60)(views.BreedListView.as_view()), name='breeds'),
    path('breeds/<int:pk>/dogs/', views.DogBreedListView.as_view(), name='breed_dogs'),
    path('dogs/', views.DogListView.as_view(), name='dogs_list'),
    path('dogs/deactivated', views.DogDeactivatedListView.as_view(), name='dogs_deactivated_list'),
    path('dogs/search/', views.DogSearchListView.as_view(), name='dog_search'), 
    path('dogs/create_update/', views.DogCreateView.as_view(), name='dog_create'),
    path('dogs/detail/<int:pk>/', views.DogDetailView.as_view(), name='dog_detail'),
    path('dogs/create_update/<int:pk>/', views.DogUpdateView.as_view(), name='dog_update'),
    path('dogs/toggle/<int:pk>/', views.toggle_activity, name='toggle_activity'),
    path('dogs/delete/<int:pk>/', views.DogDeleteView.as_view(), name='dog_delete')
]

