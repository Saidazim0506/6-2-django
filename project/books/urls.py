from django.urls import path
from .views import books_list, books_create, books_detail


urlpatterns=[
    path('books_list/', books_list, name="books_list"),
    path('books_create/', books_create, name="books_create"),
    path('books_detail/', books_detail, name="books_detail")
]