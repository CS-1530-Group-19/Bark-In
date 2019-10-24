from django.shortcuts import render
from django.http import HttpResponse

from .models import User

# Create your views here.
def index(request):

	userList = User.objects.order_by('-name')[:5]
	context = {'users':userList}
	return render(request, 'app/index.html', context)

def create_profile(request):
	return HttpResponse("Create Profile Here")

def edit_profile(request, uid):
	user = User.objects.get(pk=user_name)
	context = {'user':user}
	return render(request, 'app/edit_profile.html', context)

def view_profile(request, uid):
	return HttpResponse("View User"+str(uid)+"'s Profile Here")

def create_dog_profile(request, uid):
	return HttpResponse("Create a dog on User"+str(uid)+"'s page here")

def edit_dog_profile(request, uid, dogid):
	return HttpResponse("Edit dog"+str(dogid)+"'s profile' on User"+str(uid)+"'s page here")

def view_dog_profile(request, uid, dogid):
	return HttpResponse("View dog"+str(dogid)+"'s profile' on User"+str(uid)+"'s page here")

def view_park(request, parkid):
	return HttpResponse("View Park ID: "+str(parkid)+" Park Profile Here")

def review_park(request, parkid):
	return HttpResponse("Review Park ID: "+str(parkid)+" Park Profile Here")

def schedule(request, parkid):
	return HttpResponse("Schedule for Park ID: "+str(parkid)+" Here")