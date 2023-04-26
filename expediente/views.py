from django.shortcuts import render, redirect
from .forms import ProductorForm

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
	return render(request, 'productor/crearProductor.html', {'productor_form': productor_form})