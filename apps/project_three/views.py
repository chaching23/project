from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "project_three/index.html")


def random(request):
    if 'x' in request.session:
        request.session['x'] += 1 
    else: 
        request.session['x'] = 1

    request.session["word"]= get_random_string(length=32)

    return redirect("/") 


def clear(request):
    request.session.clear()
    return redirect("/")



