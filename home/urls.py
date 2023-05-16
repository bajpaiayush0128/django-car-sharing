from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path('register/', views.register, name="register"),
    path('logIn/', views.logIn, name="logIn"),
    path('logOut/', views.logOut, name='logOut'),
    path('PubRide/', views.PubRide, name='PubRide'),
    path('pickRide/', views.pickRide, name='pickRide'),
    path('yourRide/<int:user>/', views.yourRide, name='yourRide'),
    path('updateRide/<int:id>/', views.updateRide, name='updateRide'),
    path('riderInfo/<int:id>/', views.riderInfo, name='riderInfo'),
    path('rides/', views.rides, name='rides'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('booking/<int:pk>/', views.booking, name='booking'),
    path('success/', views.success, name='success'),
    path('decrease_counter/<int:pk>/',
         views.decrease_counter, name='decrease_counter'),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('contact/', views.contact, name='contact'),
]
