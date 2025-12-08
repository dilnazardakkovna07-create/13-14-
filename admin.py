from django.contrib import admin
from .models import Category, Manufacturer, Medicine

admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Medicine)

