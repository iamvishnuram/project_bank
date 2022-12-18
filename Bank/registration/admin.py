from django.contrib import admin
from . models import Person, District, City

admin.site.register(Person)
admin.site.register(City)
admin.site.register(District)

# Register your models here.

