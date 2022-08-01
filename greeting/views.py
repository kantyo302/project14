from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

def h_greeting(request):
    response_result = HttpResponse('everyone!')
    return response_result

class Greeting_Hello(TemplateView):
    template_name = 'index.html'
# Create your views here.
