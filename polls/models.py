from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.IntegerField()
    country = models.IntegerField()
    street = models.TextField(max_length=200)

class Permission(models.Model):
    type = models.CharField(max_length=30)
    action = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')




