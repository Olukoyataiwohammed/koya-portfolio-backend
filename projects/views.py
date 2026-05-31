from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .models import Project
from .serializers import ProjectSerializer


@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def get_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    serializer = ProjectSerializer(project)

    response = {
        "message": "project",
        "data": serializer.data
    }

    return Response(data=response, status=status.HTTP_200_OK)


@api_view(['GET'])
def featured_projects(request):
    projects = Project.objects.filter(is_featured=True)

    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def search_projects(request):
    query = request.GET.get('search', '')

    projects = Project.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(tech_stack__icontains=query)
    ).order_by('-created_at')

    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)