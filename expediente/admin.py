from django.contrib import admin

# Register your models here.

from .models import Productor, Folio, Personal

admin.site.register(Productor)
admin.site.register(Folio)
admin.site.register(Personal)