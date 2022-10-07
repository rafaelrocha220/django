from array import array
from django.db import models

# Create your models here.
class Product(models.Model): 
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(default="This is cool!")
    featured    = models.BooleanField(default=False)

