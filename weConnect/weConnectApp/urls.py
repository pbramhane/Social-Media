from django.urls import path
from . import views

urlpatterns = [
    path('', views.myLogin, name='mylogin'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('mylogout/', views.myLogout, name='mylogout'),
    #path('profile/<user>/', views.profile, name='profile'),
    path('createprofile/', views.createProfile, name='createprofile'),
    path('editprofile/<user>/', views.editProfile, name='editprofile'),
    path('addpost/', views.addPost, name='addpost'),
    path('likepost/', views.like_post, name='likepost'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow, name='unfollow'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
]