from django.db import models

# Create your models here.


class About(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)  # e.g. "Full Stack Developer"
    bio = models.TextField()

    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=80)  # percentage



