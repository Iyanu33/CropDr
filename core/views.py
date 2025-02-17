from django.shortcuts import render, get_object_or_404


# Create your views here.

def home(request):
    """docstring for home"""
    return render(request,'core/home.html')


    
