from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.name} - Stock: {self.stock} - Price: {self.price}"

