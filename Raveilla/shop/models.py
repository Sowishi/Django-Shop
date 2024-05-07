from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    image = models.ImageField( null=True, blank=True, upload_to="images/", default=None)

class WomenProducts(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    image = models.ImageField( null=True, blank=True, upload_to="images/", default=None)



class MensProducts(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    image = models.ImageField( null=True, blank=True, upload_to="images/", default=None)


class KidsProducts(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    image = models.ImageField( null=True, blank=True, upload_to="images/", default=None)

    
class Cart(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    image = models.ImageField( null=True, blank=True, upload_to="images/", default=None)





