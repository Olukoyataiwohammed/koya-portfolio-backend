from django.contrib import admin

# Register your models here.

from .models import About, Skill

admin.site.register(About)
admin.site.register(Skill)