from django.contrib import admin

from aula4.models import Person, Passport

# Register your models here.
admin.site.register((Person, Passport))
