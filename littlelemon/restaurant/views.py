from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    return render(request, 'index.html', {})
