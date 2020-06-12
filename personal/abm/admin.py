from django.contrib import admin
import os
from django.forms import Textarea
from django.db import models
from .models import Sector, Category, Charge, Destination, Agreement, Marital, Sex, Province, Location, Neighborhood, Employee, Contract, Up, Down, DownReason, Document, Training
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

class UpInline(admin.TabularInline):
    model = Up
    extra = 0
    verbose_name = "Alta"
    verbose_name_plural = "Altas"
    list_per_page = 10

class DownInline(admin.TabularInline):
    model = Down
    extra = 0
    verbose_name = "Baja"
    verbose_name_plural = "Bajas"
    list_per_page = 10

class TrainingInline(admin.TabularInline):
    model = Employee.training.through
    extra = 0
    verbose_name = "Formación"
    verbose_name_plural = "Formaciones"
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

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class DownReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('lp', 'nombre', 'apellido', 'created', 'updated')
    list_display_links = ('lp', 'nombre', 'apellido')
    search_fields = ('nombre',)
    list_per_page = 10
    #add_form_template = os.path.join(BASE_DIR, 'templates/admin/employee/change_form.html')

    fieldsets = (
        ('DATOS DE CABECERA', {
            'fields': (('lp', 'nombre', 'apellido', 'cuil', 'sexo'), 'photo', 'observaciones'),
        }),
        ('DATOS PERSONALES', {
            'fields': (('fecha_nacimiento', 'estado_civil', 'tdoc', 'ndoc'), ('provincia', 'localidad', 'barrio'), ('calle', 'numero', 'piso', 'unidad', 'cpost'), ('telefono', 'celular', 'email')),
            'classes': ('collapse',),
        }),
        ('DATOS LABORALES', {
            'fields': (('convenio', 'contrato'), ('horario', 'horas_diarias', 'horas_semanales', 'horas_mensuales'), ('obra_social', 'sindicato', 'amtedyc', 'temporada', 'cspfa', 'deportes')),
            'classes': ('collapse',),
        }),
    )

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(
                attrs={
                    'rows': 4,
                    'cols': 80
                }
            )
        }
    }

    inlines = [
        UpInline,
        SectorInline,
        CategoryInline,
        ChargeInline,
        DestinationInline,
        TrainingInline,
        DownInline
    ]

    class Media:
        css = {
             'all': ('admin/css/employee.css',)
        }

# Registers
admin.site.register(Training, TrainingAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DownReason, DownReasonAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Charge, ChargeAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Agreement,AgreementAdmin)
admin.site.register(Contract,ContractAdmin)
admin.site.register(Marital, MaritalAdmin)
admin.site.register(Sex, SexAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Employee, EmployeeAdmin)
