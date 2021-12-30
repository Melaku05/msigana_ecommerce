from django.db import models

# Create your models here.
from django.urls import reverse

from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=150, unique=True)
    product_slug = models.SlugField(max_length=150, unique=True)
    product_description = models.TextField(max_length=400, blank=True)
    product_price = models.IntegerField()
    product_images = models.ImageField()
    product_stock = models.IntegerField()
    product_is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_modified_date = models.DateTimeField(auto_now=True)

    def get_store_url(self):
        return reverse('product_detail', args=[self.category.category_slug, self.product_slug])

    def __str__(self):
        return self.product_name
