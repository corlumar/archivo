from django.urls import path
from .views import crearProductor, listarProductor, editarProductor, eliminarProductor

urlpatterns = [
	path('crear_productor/', crearProductor, name = 'crear_productor'),
	path('listar_productor/', listarProductor, name = 'listar_productor'),
	path('editar_productor/<slug:curp>', editarProductor, name = 'editar_productor'),
	path('eliminar_productor/<int:id>', eliminarProductor, name = 'eliminar_productor')

	
]