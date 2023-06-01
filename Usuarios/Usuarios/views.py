from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def home(request):
    return redirect('usuarios/')

def healthCheck(request):
    return HttpResponse('ok')