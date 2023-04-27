from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProductorForm
from .models import Productor
# 
# Create your views here.

def Home(request):
	return render(request, 'index.html')

def crearProductor(request):
	if request.method == 'POST':
		productor_form = ProductorForm(request.POST)
		if productor_form.is_valid():
			productor_form.save()
			return redirect('index')

	else:

		productor_form = ProductorForm()
	return render(request, 'productor/crear_productor.html', {'productor_form': productor_form})

def listarProductor(request):
	productores = Productor.objects.all()
	return render(request, 'expediente/listar_productor.html', {'productores':productores})

def editarProductor(request, curp):
	import logging

	productor_form = None
	error = None

	try:
		productor = Productor.objects.get(id = id)

	except Exception as e:
		return redirect('404')
	
	if request.method == 'GET':
		productor_form = ProductorForm(instance = productor)

	

	else:
		productor_form = ProductorForm(request.POST, instance = productor)
		if productor_form.is_valid():
			productor_form.save()
		return redirect('index')
	


	return render(request, 'expediente/crear_productor.html', {'productor_form': productor_form, 'error':error})

def eliminarProductor(request, id):
	productor = Productor.objects.get(id = id)
	if request.method == 'POST':
		productor.estado = False
		productor.save()
		return redirect('expediente: listar_productor')
	return render(request, 'expediente/eliminar_productor.html', {'productor': productor})