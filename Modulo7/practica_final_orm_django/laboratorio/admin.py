from django.contrib import admin

# Register your models here.

from .models import Laboratorio, DirectorGeneral, Producto



class LaboratorioAdmin(admin.ModelAdmin):
    fields=['nombre']
    list_display=('id','nombre')
    list_display_links=['nombre']
    

class DirectorGeneralAdmin(admin.ModelAdmin):
    fields=['nombre','laboratorio']
    list_display=('id','nombre','laboratorio')
    list_display_links=['nombre','laboratorio']
    ordering=('nombre','laboratorio')

class ProductoAdmin(admin.ModelAdmin):
    fields=['nombre','laboratorio','f_fabricacion','p_costo','p_venta']
    list_display=('id','nombre','laboratorio')
    list_display_links=['nombre','laboratorio']
    ordering=('nombre','laboratorio')
    list_filter=('nombre','laboratorio')
    list_per_page=4

admin.site.register(Laboratorio, LaboratorioAdmin)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
