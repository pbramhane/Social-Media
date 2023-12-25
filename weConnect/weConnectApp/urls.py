from django.urls import path
from . import views

urlpatterns = [
    path('', views.myLogin, name='mylogin'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('mylogout/', views.myLogout, name='mylogout'),
    path('profile/<int:pk>/', views.profile, name='profile')
]