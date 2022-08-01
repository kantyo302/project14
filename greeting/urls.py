from django.urls import path
from .views import h_greeting,Greeting_Hello

urlpatterns = [
    path('home/',h_greeting),
    path('home2/',Greeting_Hello.as_view())
]