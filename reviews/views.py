from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from redis.commands.search.querystring import querystring

from reviews.models import Review
from users.models import User
from reviews.forms import ReviewForm

class ReviewListView(generic.ListView):
    model = Review
    extra_context = {
        'title' : 'All Reviews'
    }
    template_name = 'reviews/reviews.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_review=True)
        return queryset

class ReviewDeactivatedListView(generic.ListView):
    model = Review
    extra_context = {
        'title' : 'Non-Active Reviews'
    }
    template_name = 'reviews/reviews.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_review=False)
        return queryset