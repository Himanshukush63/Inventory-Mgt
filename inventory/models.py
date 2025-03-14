from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('mobile', 'Mobile Phone'),
        ('laptop', 'Laptop'),
        ('smartwatch', 'Smart Watch'),
        ('buds', 'Buds'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.category})"
