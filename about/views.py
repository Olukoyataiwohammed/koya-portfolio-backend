from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import About, Skill
from .serializers import AboutSerializer, SkillSerializer


# 👉 About + Skills (combined endpoint)
@api_view(['GET'])
def about_view(request):
    about = About.objects.first()

    if not about:
        return Response(
            {"error": "No about data found"},
            status=status.HTTP_404_NOT_FOUND
        )

    skills = Skill.objects.all().order_by('-level')

    return Response({
        "about": AboutSerializer(about).data,
        "skills": SkillSerializer(skills, many=True).data
    })


# 👉 Skills only (separate endpoint - BEST PRACTICE)
@api_view(['GET'])
def skills_view(request):
    skills = Skill.objects.all().order_by('-level')

    return Response({
        "count": skills.count(),
        "results": SkillSerializer(skills, many=True).data
    })