from django.urls import path
from .views import users_list, users_create, users_detail


urlpatterns=[
    path('users_list/', users_list, name="users_list"),
    path('users_create/', users_create, name="users_create"),
    path('users_detail/', users_detail, name="users_detail"),
]