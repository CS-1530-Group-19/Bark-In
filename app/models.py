from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

# https://docs.djangoproject.com/en/2.2/ref/models/fields

def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)
	# THIS NEEDS A CHECK
	# https://stackoverflow.com/questions/8189800/django-store-user-image-in-model
	# Based on that 

# Create your models here.
class Dog(models.Model):
	name = models.CharField(max_length=150, default="Un-named")
	dog_pfp = models.FileField(upload_to='dogpics', blank=True, null=True)
	breed = models.CharField(max_length=150, null=True)
	dog_size = models.CharField(max_length=140, null=True) #change to S/M/L
	temperament = models.PositiveIntegerField(blank=True)
	activity_level = models.PositiveIntegerField(blank=True)
	volume = models.PositiveIntegerField(blank=True)
	notes = models.CharField(max_length=512,null=True)
	def __str__(self):
		return self.name

class UserProfileManager(models.Manager):
         pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=512,null=True)
    dogs = models.ManyToManyField(Dog, blank=True)
    favoritePark = models.CharField(max_length = 150, default = 'none')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class ParkReview(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	review = models.CharField(max_length=1024, null=True, blank=True)
	star_rating = models.PositiveIntegerField(default=0,blank=True)
	timeposted = models.DateField(auto_now=True)
	def __str__(self):
		return self.user.username

class Schedule(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True,blank=True)
    date = models.DateField(null=False)
    t_start = models.DurationField(null=False)
    t_end = models.DurationField(null=False)
    def __str__(self):
        return self.dog.name

class Park(models.Model):
    name = models.CharField(max_length=150, unique=False, null=True)
    lat = models.FloatField(blank=False)
    lon = models.FloatField(blank=False)
    info = models.CharField(max_length=512,null=True)
    address = models.CharField(max_length=512,null=True)
    fenced_in = models.BooleanField(default=False)
    off_leash = models.BooleanField(default=False)
    schedules = models.ManyToManyField(Schedule,blank=True)
    reviews = models.ManyToManyField(ParkReview, blank=True)
    def __str__(self):
        return self.name
