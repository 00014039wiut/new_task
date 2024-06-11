from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    rating = models.IntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
