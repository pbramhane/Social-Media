from django.contrib import admin
from .models import Profile, Post

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'about')

class PostAdmin(admin.ModelAdmin):
    list_display = ('caption',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
