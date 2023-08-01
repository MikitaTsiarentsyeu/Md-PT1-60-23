from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('success', views.success, name='success'),
    path('add', views.add, name='add'),
    path('api-auth/', include('rest_framework.urls')),
    
]