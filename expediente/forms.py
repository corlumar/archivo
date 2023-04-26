from django import forms
from .models import Productor

class ProductorForm(forms.ModelForm):
	class Meta:
		model = Productor
		fields = ['nombre', 'apell_pat', 'apell_mat', 'genero', 'curp']