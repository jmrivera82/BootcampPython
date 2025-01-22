
from django.contrib import admin

# Register your models here.

from .models import Proveedor, Mercaderista, Producto



class ProveedorAdmin(admin.ModelAdmin):
    fields=['nombre']
    list_display=('id','nombre')
    list_display_links=['nombre']
    

class MercaderistaAdmin(admin.ModelAdmin):
    fields=['nombre','proveedor']
    list_display=('id','nombre','proveedor')
    list_display_links=['nombre','proveedor']
    ordering=('nombre','proveedor')

class ProductoAdmin(admin.ModelAdmin):
    fields=['nombre','proveedor','f_fabricacion','p_costo','p_venta']
    list_display=('id','nombre','proveedor')
    list_display_links=['nombre','proveedor']
    ordering=('nombre','proveedor')
    list_filter=('nombre','proveedor')
    list_per_page=8

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Mercaderista, MercaderistaAdmin)
