from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse(
        "<h1>Hello, World! This is the home page of my Django application.</h1>"
        "<p>Here is my small change for step 3</p>"    
)

def about(request):
    return HttpResponse("<h1>About Page </h1> <p>This is the about page of my Django application.</p>")