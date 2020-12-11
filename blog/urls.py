""" Importieren der Django-Funktion path und alle views 
aus der blog-Applikation.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]