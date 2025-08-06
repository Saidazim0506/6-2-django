from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def users_list(request: HttpRequest):
    return HttpResponse("<h1>Users royhati</h1>")

def users_create(request: HttpRequest):
    return HttpResponse("<h1>Users yararish</h1>")

def users_detail(request: HttpRequest):
    return HttpResponse("<h1>Users haqida batafsil</h1>")
