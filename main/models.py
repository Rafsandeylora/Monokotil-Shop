from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('hat', 'Hat'),
        ('merchandise', 'Merchandise'),
        ('ball', 'Ball'),
        ('handsign', 'Hansign'),
        ('shoes', 'Shoes'),
    ]
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stocks = models.IntegerField()
    rarity = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True,null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
