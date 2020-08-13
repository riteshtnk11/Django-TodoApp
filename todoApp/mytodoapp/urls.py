from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #This will call the index function inside views file
    
]