from django.urls import path
from .views import (
    project_list,
    featured_projects,
    search_projects,
    get_project,
)

urlpatterns = [
    path('', project_list, name='project-list'),
    path('featured/', featured_projects, name='featured-projects'),
    path('search/', search_projects, name='search-projects'),
    path("projects/<int:project_id>/", get_project, name="get-project"),
]