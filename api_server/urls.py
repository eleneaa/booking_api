"""
URL configuration for api_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import book_api
from book_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/occupied', views.get_occupied_book, name="Occupied"),
    path('books/free', views.get_free_book, name="Free"),
    path('books/last', views.get_last_book, name="Last"),
    path('books/confirmed', views.get_confirmed_book, name="Confirmed"),
    path('users/authenticate', views.authenticate, name="authenticate"),
    path('users/register_user', views.register_user, name="register_user"),
    path('users', views.get_users, name="Users"),
    path('books/all', views.get_all_books, name="All"),
]
