from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(upload_to='projects/')

    tech_stack = models.CharField(max_length=255)  
    # e.g. "React, Django, PostgreSQL"

    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title