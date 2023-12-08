from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {'page': 'Golden Future Institute'}
    return render(request, "home/index.html", context)
    

def courses(request):
    context = {'page': 'GFI | Courses'}
    return render(request, 'home/courses.html', context)

def languages(request):
    context = {'page': 'GFI | Languages'}
    return render(request, "home/languages.html", context)

def tuition(request):
    context = {'page': 'GFI | Tuition'}
    return render(request, "home/tuition.html", context)

def bridgecourse(request):
    context = {'page': 'GFI | Bridge Course'}
    return render(request, "home/bridgecourse.html", context)
    
def career(request):
    context = {'page': 'GFI | Career'}
    return render(request, "home/career.html", context)

def gallery(request):
    context = {'page': 'GFI | Gallery'}
    return render(request, "home/gallery.html", context)

def contact(request):
    context = {'page': 'GFI | Contact'}
    return render(request, "home/contact.html", context)