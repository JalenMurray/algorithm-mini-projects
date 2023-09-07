from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse

from projects.models import Project

class ProjectList(ListView):
  model = Project


class ProjectDetail(DetailView):
  model = Project
