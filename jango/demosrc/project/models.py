from django.db import models

# Create your models here.
class ContactUs(models.Model):
	name  	 = models.CharField(max_length=150)
	email 	 = models.CharField(max_length=50)
	phone 	 = models.CharField(max_length=12)
	complain = models.TextField()