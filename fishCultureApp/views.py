from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


def home_view(request):
    if request.is_ajax and request.method == "GET":
        candidate = request.GET.get("buttonOn")
        print(candidate)
        return render(request, 'home.html', status=200)
    
    return render(request,'home.html')

def url_view(request,value):
    return render(request,'home.html')