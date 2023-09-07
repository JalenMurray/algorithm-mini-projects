from django.urls import path
from django.views.generic import TemplateView
from projects.views import ProjectList, ProjectDetail


app_name = 'projects'
urlpatterns = [
    path('', ProjectList.as_view(), name='index'),
    path('<int:pk>', ProjectDetail.as_view(), name='detail')
]

