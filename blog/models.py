from django.conf import settings
from django.db import models
from twilio.rest import Client
import os
import environ
env = environ.Env(

)
environ.Env.read_env()

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    rating = models.IntegerField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    discount = models.IntegerField(default=0)

    def get_attributes(self) -> list[dict]:
        product_attributes = ProductAttribute.objects.filter(product=self)
        attributes = []
        for pa in product_attributes:
            attributes.append({
                'attribute_key': pa.attribute.key_name,
                'attribute_value': pa.attribute_value.value_name
            })  # [ {},{},{}]
        return attributes

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Attribute(models.Model):
    key_name = models.CharField(max_length=125, unique=True)

    def __str__(self):
        return self.key_name


class AttributeValue(models.Model):
    value_name = models.CharField(max_length=125, unique=True)

    def __str__(self):
        return self.value_name


class ProductAttribute(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    attribute_value = models.ForeignKey('AttributeValue', on_delete=models.CASCADE)


class SMS(models.Model):
    to_number = models.TextField(max_length=50)

    def __str__(self):
        return self.to_number

    def save(self, *args, **kwargs):
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='You have successfully registered!',
            from_='+13193083049',
            to=self.to_number,
        )
        print(message.sid)
        return super(SMS, self).save(*args, **kwargs)
