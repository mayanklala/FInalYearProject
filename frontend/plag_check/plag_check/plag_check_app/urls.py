from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('',views.home,name='home'),
        path('check_plag',views.check_plag,name='check_plag'),
]