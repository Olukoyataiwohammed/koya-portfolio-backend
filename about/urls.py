from django.urls import path
from .views import about_view, skills_view

urlpatterns = [
    path("about/", about_view, name="about"),
    path("skills/", skills_view, name="skills"),
]