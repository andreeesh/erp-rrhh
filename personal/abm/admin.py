from django.contrib import admin
import os
from .models import Sector, Category, Charge, Destination, Contract, Marital, Sex, Province, Location, Neighborhood, Employee
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Inlines
class SectorInline(admin.TabularInline):
    model = Employee.sector.through
    extra = 0
    verbose_name = "Sector"
    verbose_name_plural = "Sectores"
    list_per_page = 10

class CategoryInline(admin.TabularInline):
    model = Employee.category.through
    extra = 0
    verbose_name = "Categoría"
    verbose_name_plural = "Categorías"
    list_per_page = 10

class DestinationInline(admin.TabularInline):
    model = Employee.destination.through
    extra = 0
    verbose_name = "Destino"
    verbose_name_plural = "Destinos"
    list_per_page = 10

class ChargeInline(admin.TabularInline):
    model = Employee.charge.through
    extra = 0
    verbose_name = "Tarea / Cargo"
    verbose_name_plural = "Tareas / Cargos"
    list_per_page = 10

# Admins
class SectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class ChargeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class MaritalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class SexAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class AgreementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('lp', 'nombre', 'created', 'updated')
    list_display_links = ('lp', 'nombre')
    search_fields = ('nombre',)
    list_per_page = 10
    #add_form_template = os.path.join(BASE_DIR, 'templates/admin/employee/change_form.html')

    fieldsets = (
        ('DATOS DE CABECERA', {
            'fields': ('lp', 'nombre', 'apellido', 'cuil', 'photo', 'sexo'),
        }),
        ('DATOS PERSONALES', {
            'fields': ('fecha_nacimiento', 'tdoc', 'ndoc', 'estado_civil', 'calle', 'numero', 'piso', 'unidad', 'provincia', 'localidad', 'barrio', 'email', 'telefono', 'celular', 'cpost', 'observaciones'),
            'classes': ('collapse',),
        }),
        ('DATOS LABORALES', {
            'fields': ('fechadealta', 'contrato', 'horario'),
            'classes': ('collapse',),
        }),
    )

    inlines = [
        SectorInline,
        CategoryInline,
        ChargeInline,
        DestinationInline,
    ]

    class Media:
        css = {
             'all': ('admin/css/employee.css',)
        }

# Registers
admin.site.register(Sector, SectorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Charge, ChargeAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Marital, MaritalAdmin)
admin.site.register(Sex, SexAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Employee, EmployeeAdmin)
