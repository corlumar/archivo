from django.db import models

# Create your models here.

class Productor(models.Model):
	id = models.BigAutoField(max_length = 100, primary_key = True)
	nombre = models.CharField(max_length = 100, blank = False, null = False)
	apell_pat = models.CharField(max_length = 50, blank = True, null = True)
	apell_mat = models.CharField(max_length = 50, blank = True, null = True)
	generos = [
        ("H", "Hombre"),
        ("M", "Mujer"),
    ]
	genero = models.CharField(max_length = 1, choices = generos)
	curp = models.CharField(max_length = 18, blank = False, null = False)

