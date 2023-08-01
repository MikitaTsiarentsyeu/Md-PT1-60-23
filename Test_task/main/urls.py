from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('success', views.success, name='success'),
    path('add', views.add, name='add'),
    
]