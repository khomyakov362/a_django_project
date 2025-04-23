from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail

from dogs.models import Breed
from dogs.models import Dog

def get_breed_cache():
    if settings.CACHE_ENABLED:
        key = 'breed_list'
        breed_list = cache.get(key)
        if breed_list is None:
            breed_list = Breed.objects.all()
            cache.set(key, breed_list)
            return breed_list
    else:
        return Breed.objects.all()
    
def send_views_mail(dog, owner_email, views):
    send_mail(
        subject=f'{views} views of {dog}',
        message=f'Harray! Your dog {dog} has got {views} views already!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[owner_email]
    )
