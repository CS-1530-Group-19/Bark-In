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

class ParkReview(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
	review = models.CharField(max_length=512, null=True, blank=True)
	star_rating = models.PositiveIntegerField(default=0,blank=True)
	timeposted = models.DateField(auto_now=True)
	def __str__(self):
		return self.user.name

class Park(models.Model):
	name = models.CharField(max_length=140, unique=False, null=True)
	lat = models.IntegerField(blank=False)
	lon = models.IntegerField(blank=False)
	info = models.CharField(max_length=512,null=True)
	address = models.CharField(max_length=512,null=True)
	star_rating = models.PositiveIntegerField(default=0,blank=True)
	num_ratings = models.PositiveIntegerField(default=0,blank=True)
	fenced_in = models.BooleanField(default=False)
	off_leash = models.BooleanField(default=False)
	reviews = models.ManyToManyField(ParkReview, blank=True)
	def __str__(self):
		return self.name

class Schedule(models.Model):
	dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=False)
	park = models.ForeignKey(Park, on_delete=models.CASCADE, null=False)
	time_start = models.DateField(null=False)
	duration = models.DurationField(null=False)
	def __str__(self):
		return self.dog.name
