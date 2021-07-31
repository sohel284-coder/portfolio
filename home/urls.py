from django.urls import path, include
from home.views import *

urlpatterns = [
    path('', home, name='home'),
    path('skill', skill, name='skill'),
    path('experience', experience, name='experience'),
    path('project', project, name='project'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('api/all-project/', AllProjectListCreateAPIView.as_view(), ),
    path('api/pers-project/', PersonalProjectListCreateAPIView.as_view(), ),
    path('api/prof-project/', ProfessionalProjectListCreateAPIView.as_view(), ),


]