from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Productor, Folio, Personal



# Register your models here.


class ProductorResource(resources.ModelResource):
	class Meta:
		model = Productor

class ProductorAdmin(ImportExportModelAdmin):
	search_fields = ['nombre']
	list_display = ('nombre', 'apell_pat', 'apell_mat', 'genero', 'estado', 'curp')
	resources_class = ProductorResource

class FolioResource(resources.ModelResource):
	class Meta:
		model = Folio


class FolioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['id']
	list_display = ('id', 'productor_id', 'fecha_solicitud')
	resources_class = FolioResource

class PersonalResource(resources.ModelResource):
	class Meta:
		model = Personal

class PersonalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['id']
	list_display = ('id', 'nombre')
	resources_class = PersonalResource

admin.site.register(Productor, ProductorAdmin)
admin.site.register(Folio, FolioAdmin)
admin.site.register(Personal, PersonalAdmin)