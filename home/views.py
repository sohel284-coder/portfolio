from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import permissions, serializers
from home.serializers import ProjectSerializer

from home.models import *


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contact_details = request.POST.get('desc')
        cont = ClientContact(name=name, email=email, phone=phone, subject=subject, contact_details=contact_details)
        cont.save()
        data = {
            'client_name':name,
            'client_email': email,
            'client_phone': phone,
            'subject': subject,
            'message': contact_details,
        }
        subject = subject
        reciever_email = []
        email_from = email
        reciever_email.append(settings.EMAIL_HOST_USER, )
        html_message = render_to_string('contact/email.html', {'data': data })
        send_mail(subject, None, from_email=email_from, recipient_list=reciever_email, html_message=html_message, fail_silently=False, )
        messages.success(request, 'Your message has been sent')

    return render(request, 'home.html', )


def skill(request):
    return render(request, 'portfolio/skill.html', )

def experience(request):
    return render(request, 'portfolio/experience.html', )


def project(request):
    return render(request, 'portfolio/project.html', )


def about(request):
    return render(request, 'portfolio/about.html', )

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contact_details = request.POST.get('desc')
        cont = ClientContact(name=name, email=email, phone=phone, subject=subject, contact_details=contact_details)
        cont.save()
        
        data = {
            'client_name':name,
            'client_email': email,
            'client_phone': phone,
            'subject': subject,
            'message': contact_details,
        }
        subject = subject
        reciever_email = []
        email_from = email
        reciever_email.append(settings.EMAIL_HOST_USER, )
        html_message = render_to_string('contact/email.html', {'data': data })
        send_mail(subject, None, from_email=email_from, recipient_list=reciever_email, html_message=html_message, fail_silently=False, )
        messages.success(request, 'Your message has been sent')
        return redirect('home')
    return render(request, 'portfolio/contact.html', )








class AllProjectListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectSerializer
    queryset = Project.objects.all() 

class PersonalProjectListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(is_personal=True, )

class ProfessionalProjectListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(is_professional=True, )





    

   




