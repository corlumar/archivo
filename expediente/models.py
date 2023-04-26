from django.db import models

# Create your models here.

class Productor(models.Model):
	id = models.BigAutoField(primary_key = True)
	nombre = models.CharField('Nombre', max_length = 100, blank = False, null = False)
	apell_pat = models.CharField('apell_pat', max_length = 50, blank = True, null = True)
	apell_mat = models.CharField('apell_mat', max_length = 50, blank = True, null = True)
	generos = [
        ("H", "Hombre"),
        ("M", "Mujer"),
    ]
	genero = models.CharField('Género', max_length = 1, choices = generos)
	curp = models.CharField('CURP',  max_length = 18, blank = False, null = False)

	class Meta:
		verbose_name = 'Productor'
		verbose_name_plural = 'Productores'
		ordering = ['nombre']


	def __str__(self):
		return f"{self.nombre} {self.apell_pat} {self.apell_mat}"


class Folio(models.Model):
	id = models.CharField(max_length = 25, primary_key = True, blank = False, null = False)
	productor_id = models.ForeignKey(Productor, on_delete = models.CASCADE)
	fecha_solicitud = models.DateField('Fecha de Solicitud')

		
	class Meta:
		verbose_name = 'Folio'
		verbose_name_plural = 'Folios'
		ordering = ['id']  

	def __str__(self):
	     return self.id

class Personal(models.Model):
	id = id = models.BigAutoField(primary_key = True)
	nombre = models.CharField(max_length = 100, blank = False, null = False)

	class Meta:
		verbose_name = 'Personal'
		verbose_name_plural = 'Personal'
		ordering = ['id']  

	def __str__(self):
	     return self.id
