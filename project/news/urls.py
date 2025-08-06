from tkinter.font import names

from django.urls import path
from .views import news_list, news_create, news_detail


urlpatterns=[
    path('', news_list, name="news_list"),
    path('news_create/', news_create, name="news_create"),
    path('news_detail/', news_detail, name="news_detail")
]