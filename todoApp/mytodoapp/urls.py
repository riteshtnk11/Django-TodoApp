from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"), #This will call the index function inside views file
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task")
]