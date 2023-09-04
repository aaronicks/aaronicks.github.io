from django.db import models

# Create your models here.
class Laptop(models.Model):
	ram 		= models.IntegerField(default=0)
	storage 	= models.CharField(max_length=10)
	graphics	= models.CharField(max_length=20)
	wireless	= models.CharField(max_length=20)
	usb_port	= models.CharField(max_length=20)
	battery		= models.CharField(max_length=30)
	os 			= models.CharField(max_length=50)
	screen_size = models.DecimalField(decimal_places=2, max_digits=8, default=00.00)
	price 		= models.DecimalField(decimal_places=2, max_digits=10000)
