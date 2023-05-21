from django.db import models
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
class mashalachicken(models.Model):
	half = models.IntegerField()
	full = models.IntegerField()
class tavadhosa(models.Model):
	masaladhosa = models.IntegerField()
	paneerdhosa = models.IntegerField()
class registerResturant(models.Model):
	
    restaurantName = models.CharField(max_length=50)
    ownerName = models.CharField(max_length=50)
    GSTNumber = models.CharField(max_length=50)
    FSSAINumber = models.CharField(max_length=50)
    Address= models.CharField(max_length=50)
    PhoneNo= models.CharField(max_length=50)
    UserName= models.CharField(max_length=50)
    Email= models.CharField(max_length=50)

class registerResturantNewModels(models.Model):
	
    restaurantName = models.CharField(max_length=50)
    ownerName = models.CharField(max_length=50)
    GSTNumber = models.CharField(max_length=50)
    FSSAINumber = models.CharField(max_length=50)
    Address= models.CharField(max_length=50)
    PhoneNo= models.CharField(max_length=50)
    UserName= models.CharField(max_length=50)
    Email= models.CharField(max_length=50)
class registerresturantNewModels2(models.Model):
	
    restaurantName = models.CharField(max_length=50)
    ownerName = models.CharField(max_length=50)
    GSTNumber = models.CharField(max_length=50)
    FSSAINumber = models.CharField(max_length=50)
    Address= models.CharField(max_length=50)
    PhoneNo= models.CharField(max_length=50)
    UserName= models.CharField(max_length=50)
    Email= models.CharField(max_length=50)
