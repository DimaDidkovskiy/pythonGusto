from django.contrib import admin
from.models import Category, Dishes, Event, Banners, UserMessages

# Register your models here.

admin.site.register(Category)
admin.site.register(Dishes)
admin.site.register(Event)
admin.site.register(Banners)
admin.site.register(UserMessages)
