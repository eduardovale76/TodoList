from django.urls import path
from .views import index, updateTask

urlpatterns = [
    path('', index, name='index'),
    path('update/<int:pk>/', updateTask, name='updateTask'),
]
