from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=55, )
    profile_image = models.ImageField(upload_to='profile_pic')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100, )
    description = models.CharField(max_length=255, )
    git_url = models.URLField(null=True, blank=True, )
    is_personal = models.BooleanField(default=False, )
    is_professional = models.BooleanField(default=False, )
    is_deployed = models.BooleanField(default=False, )
    deploy_url = models.URLField(null=True, blank=True, )
    image = models.ImageField(upload_to='project_pics', null=True, blank=True, )
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.name



class ClientContact(models.Model):
    name = models.CharField(max_length=63, )
    email = models.CharField(max_length=255, )
    phone = models.CharField(max_length=17, )
    subject = models.CharField(max_length=100, null=True, blank=True, )
    contact_details = models.TextField()

    def __str__(self):
        return self.name



   
        
