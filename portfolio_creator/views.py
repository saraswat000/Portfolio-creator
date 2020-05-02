from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import User
import random
import simplejson as json
def hello(request):
    if request.method == 'POST':
        bad_chars = [';', ':', '!', "*", "." ,"-" ,","] 
        user = User()
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.linkedin = request.POST.get('linkedin')
        user.github = request.POST.get('github')
        # user.image = request.POST.get('image')
        user.summary = request.POST.get('bio')
        l = request.POST.get('skills')
        ls = l.split(',')
        user.skills = json.dumps(ls)
        p = request.POST.get('languages')
        ps = p.split(',')
        user.languages = json.dumps(ps)
        userid = request.POST.get('email').split('@')[0]
        for i in bad_chars:
            userid = userid.replace(i,'')
        print(userid)
        user.userid = userid
        user.course = request.POST.get('course')
        user.college = request.POST.get('college')
        user.image = request.POST.get('image')
        link = "localhost:8000/portfolio/" + user.userid
        user.save()
        return render(request, 'portfolio_creator/output.html',{"link" : link})
    else:
        return render(request, 'portfolio_creator/input.html')
def index(request, slug):
    print(slug)
    details = User.objects.all()
    l = []
    for i in details:
        if i.userid == slug:
            l.append(i)
    
    return render(request, 'portfolio_creator/index.html', {"details" : l})


def about(request, slug):
   

    details = User.objects.filter(userid__iexact = slug)
    obj = details.first()
    jsonDec = json.decoder.JSONDecoder()
    skills = jsonDec.decode(obj.skills)
    languages = jsonDec.decode(obj.languages)    
    name = obj.name.split()
    return render(request, 'portfolio_creator/about.html' , {"name":name,"user" : obj , "skills" : skills , "languages" : languages})
