from django.urls import path
from django.views.generic import TemplateView
from projects.views import ProjectList

app_name = 'algorithms'
urlpatterns = [
    path('', ProjectList.as_view(), name='index'),
]