from django.template.response import TemplateResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'blog/index.html')