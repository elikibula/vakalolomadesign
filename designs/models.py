from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
