from django.contrib import admin
from . models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'title')


admin.site.register(Profile, ProfileAdmin)