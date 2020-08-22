from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    userid = models.CharField(primary_key=True,max_length=50,default="sample")
    linkedin = models.TextField(max_length=500)
    github = models.TextField(max_length=500)
    summary = models.TextField(max_length=200)
    skills = models.TextField(max_length=500)
    projectsTitles = models.TextField(max_length=500)
    image = models.ImageField(upload_to='portfolio_creator/images/')
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    projectsSummary = models.TextField(max_length=500)
    projectsLink = models.TextField(max_length=200)