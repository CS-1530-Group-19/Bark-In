"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
from .models import Park,UserProfile
from app.forms import (EditProfileForm, ProfileForm)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def index(request):
    """Renders the home page."""
    all_parks = Park.objects.all()
    template = loader.get_template('app/index.html')
    context = {
        'all_parks' : all_parks,
        'title':'Home Page',
        'year':datetime.now().year,
        }
    return HttpResponse(template.render(context, request))

    """assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )"""

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'year':datetime.now().year,
        }
    )
	
def login(request):
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/login.html',
		{
			'title':'Login',
			'year':datetime.now().year
		}
	)
	
def sign_up(request):
	assert isinstance(request, HttpRequest)
	return render(
		request, 
		'app/signup.html',
		{
			'title':'Sign Up',
			'year':datetime.now().year
		}
	)
	
def about(request):
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/about.html',
		{
			'title':'Login',
			'year':datetime.now().year
		}
	)

def create_profile(request):
	return HttpResponse("Create Profile Here")

def view_profile(request, uid):
	return HttpResponse("View User "+str(uid)+"'s Profile Here")

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

@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)  # request.FILES is show the selected image or file

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        args = {}
        # args.update(csrf(request))
        args['form'] = form 
        args['profile_form'] = profile_form
        return render(request, 'app/edit_profile.html', args)