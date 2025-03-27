from django.db import models

from users.models import NULLABLE

class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='breed')
    description = models.CharField(max_length=1000, verbose_name='description', **NULLABLE)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'breed'
        verbose_name_plural = 'breed'

class Dog(models.Model):
    name = models.CharField(max_length=150, verbose_name='dog_name')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='breed')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE)
    birth_date = models.DateField(**NULLABLE, verbose_name='birth_date')

    def __str__(self):
        return f'{self.name} ({self.breed})'
    
    class Meta:
        verbose_name = 'dog'
        verbose_name_plural = 'dogs'