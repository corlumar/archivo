from django.urls import path
from .views import crearProductor

urlpatterns = [
	path('crear_productor/', crearProductor, name = 'crearProductor')
	
]