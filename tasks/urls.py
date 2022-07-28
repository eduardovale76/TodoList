from django.urls import path
from .views import index, updateTask, deleteTask

urlpatterns = [
    path('', index, name='index'),
    path('update/<int:pk>/', updateTask, name='updateTask'),
    path('deletetask/<int:pk>/', deleteTask, name='deletetask'),
]
