from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    userid = models.CharField(primary_key=True,max_length=15,default="sample")
    linkedin = models.TextField(max_length=500)
    github = models.TextField(max_length=500)
    summary = models.TextField(max_length=200)
    skills = models.TextField(max_length=500)
    projects = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)