from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank' : True, 'null' : True}

class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(max_length=150, verbose_name='First name', default='Anonymous')
    last_name = models.CharField(max_length=150, verbose_name='Last Name', default='Anonymous')
    phone = models.CharField(max_length=35, verbose_name='Phone Number', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Telegram Username', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}' 

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
