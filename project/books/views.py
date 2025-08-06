from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def books_list(request: HttpRequest):
    return HttpResponse("<h1>Kitoblar royhati</h1>")

def books_create(request: HttpRequest):
    return HttpResponse("<h1>Kitoblar yararish</h1>")

def books_detail(request: HttpRequest):
    return HttpResponse("<h1>Kitoblar haqida batafsil</h1>")
