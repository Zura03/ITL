from unittest.util import _MAX_LENGTH
from django.db import models


class AuthorModel(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    email = models.EmailField()
    
    class Meta:
        ordering = ('fname',)
        
class PublisherModel(models.Model):
    name = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    
    class Meta:
        ordering = ('name',)
        
class BookModel(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateField()
    authors = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    publisher = models.OneToOneField(PublisherModel, on_delete = models.CASCADE)
    class Meta:
        ordering = ('title',)
        
#q2

class ProductModel(models.Model):
    title = models.CharField(max_length = 100)
    price = models.PositiveIntegerField()
    description = models.TextField()


#q3

class HumanModel(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)