from django.urls import path

from reviews.apps import ReviewsConfig
from reviews import views

app_name = ReviewsConfig.name

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review_list'),
    path('deactivated/', views.ReviewDeactivatedListView.as_view(), name='review_deactivated_list'),

]