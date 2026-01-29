from django.shortcuts import render
from .models import Project, Skill, Experience


# Create your views here.
def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()

    context = {
        "projects": projects,
        "skills": skills,
        "experiences": experiences,
    }
    return render(request, "portfolio/index.html", context)
