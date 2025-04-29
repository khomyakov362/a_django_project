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
from reviews.utils import slug_generator
from users.models import UserRoles

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

class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/create.html'
    extra_context = {
        'title' : 'Write a review'
    }

    def form_valid(self, form):
        if self.request.user.role not in (UserRoles.USER, UserRoles.ADMIN):
            return HttpResponseForbidden()
        self.object = form.save()
        print(self.object.slug)
        if self.object.slug == 'temp_slug':
            self.object.slug = slug_generator()
            print(self.object.slug)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ReviewDetailView(LoginRequiredMixin, generic.DetailView):
    model = Review
    template_name = 'reviews/detail.html'
    etra_context = {
        'title' : 'See review'
    }

class ReviewUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/update.html'
    extra_context = {
        'title' : 'Edit review'
    }

    def get_success_url(self):
        return reverse('reviews:review_detail')
    
    def get_object(self, queryset = None):
        self.object = super().get_object(queryset=queryset)
        if self.object.author != self.request.user and self.request.user not in (UserRoles.ADMIN, UserRoles.MODERATOR):
            raise PermissionDenied()
        return self.object

class ReviewDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Review
    template_name = 'reviews/delete.html'
    permission_required = 'reviews.delete_review'

    def get_success_url(self):
        return reverse('reviews:reviews_list')

def review_toggle_activity(request, slug):
    review_item = get_object_or_404(Review, slug=slug)
    review_item.sign_of_review = not review_item.sign_of_review
    review_item.save()
    if not review_item.sign_of_review:
        return redirect(reverse('reviews:reviews_deactivated_list'))
    else:
        return redirect(reverse('reviews:reviews_list'))