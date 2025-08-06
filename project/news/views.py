from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def news_list(request: HttpRequest):
    return HttpResponse("<h1>News royhati</h1>")

def news_create(request: HttpRequest):
    return HttpResponse("<h1>News yararish</h1>")

def news_detail(request: HttpRequest):
    return HttpResponse("<h1>News haqida batafsil</h1>")