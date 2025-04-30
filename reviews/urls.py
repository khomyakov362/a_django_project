from django.urls import path

from reviews.apps import ReviewsConfig
from reviews import views

app_name = ReviewsConfig.name

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review_list'),
    path('deactivated/', views.ReviewDeactivatedListView.as_view(), name='review_deactivated_list'),
    path('review/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('review/detail/<slug:slug>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('review/update/<slug:slug>/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('review/delete/<slug:slug>/', views.ReviewDeleteView.as_view(), name='review_delete'),
    path('review/toggle/<slug:slug>/', views.review_toggle_activity, name='review_toggle_activity'),

]