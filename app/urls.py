from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('login', views.login, name='login'),
	path('logout_view', views.logout_view, name='logout_view'), 
	path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_profile/<int:uid>', views.view_profile, name='view_profile'),
    path('view_profile/<int:uid>/add_dog', views.add_dog, name='add_dog'),
    path('view_profile/<int:uid>/edit_dog_profile/<int:dogid>', views.edit_dog_profile, name='edit_dog_profile'),
    path('view_profile/<int:uid>/view_dog/<int:dogid>', views.view_dog, name='view_dog'),
    path('view_park/<int:parkid>', views.view_park, name='view_park'),
    path('view_park/<int:parkid>/review_park', views.review_park, name='review_park'),
    path('view_park/<int:parkid>/schedule', views.schedule, name='schedule'),
]