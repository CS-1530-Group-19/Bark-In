from django.db import models
import os

# https://docs.djangoproject.com/en/2.2/ref/models/fields

def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)
	# THIS NEEDS A CHECK
	# https://stackoverflow.com/questions/8189800/django-store-user-image-in-model
	# Based on that 

# Create your models here.
class Dog(models.Model):
	name = models.CharField(max_length=140, default="Un-named")
	dog_pfp = models.FileField(upload_to=get_image_path, blank=True, null=True)
	breed = models.CharField(max_length=140,null=True)
	dog_size = models.CharField(max_length=140,null=True)
	temperament = models.PositiveIntegerField(default=5,blank=True)
	activity_level = models.PositiveIntegerField(default=5,blank=True)
	volume = models.PositiveIntegerField(default=5,blank=True)
	notes = models.CharField(max_length=512,null=True)
	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=140, unique=True, null=True)
	password = models.CharField(max_length=140, blank=False, null=True)
	email = models.EmailField(max_length=256,null=True)
	bio = models.CharField(max_length=512,null=True)

	dogs = models.ManyToManyField(Dog, blank=True)
	def __str__(self):
		return self.name


