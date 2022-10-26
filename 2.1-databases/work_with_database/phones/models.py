from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    lte_exists = models.BooleanField()


def get_absolute_url(self):
    return reverse('phone_detail', kwargs={'slug': self.slug})
