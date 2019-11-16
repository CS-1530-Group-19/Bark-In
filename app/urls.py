from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('login', views.login, name='login'),
	path('logout_view', views.logout_view, name='logout_view'),
	path('signup', views.sign_up, name='signup'),
	path('about', views.about, name='about'),
    path('create_profile', views.create_profile, name='create_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_profile/<int:uid>', views.view_profile, name='view_profile'),
    path('view_profile/<int:uid>/create_dog_profile', views.create_dog_profile, name='create_dog_profile'),
    path('view_profile/<int:uid>/edit_dog_profile/<int:dogid>', views.edit_dog_profile, name='edit_dog_profile'),
    path('view_profile/<int:uid>/view_dog_profile/<int:dogid>', views.view_dog_profile, name='view_dog_profile'),
    path('view_park/<int:parkid>', views.view_park, name='view_park'),
    path('view_park/<int:parkid>/review_park', views.review_park, name='review_park'),
    path('view_park/<int:parkid>/schedule', views.schedule, name='schedule'),
]