from django.db import models
from django.forms import Textarea

DNI_TYPES = (
    ('1', 'DNI'),
    ('2', 'LC'),
    ('3', 'LE'),
)

YES_NO = (
    ('0', 'No'),
    ('1', 'Si'),
)

# Sector model
class Sector(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        ordering = ['name']

    def __str__(self):
        return self.name

# Category model
class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

# Charge model
class Charge(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Tarea / Cargo'
        verbose_name_plural = 'Tareas / Cargos'
        ordering = ['name']

    def __str__(self):
        return self.name

# Destination model
class Destination(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'
        ordering = ['name']

    def __str__(self):
        return self.name

# Contract model
class Contract(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['name']

    def __str__(self):
        return self.name

# Marital model
class Marital(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados civiles'
        ordering = ['name']

    def __str__(self):
        return self.name

# Province model
class Province(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ['name']

    def __str__(self):
        return self.name

# Location model
class Location(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        ordering = ['name']

    def __str__(self):
        return self.name

# Neighborhood model
class Neighborhood(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'
        ordering = ['name']

    def __str__(self):
        return self.name

# Agreement model
class Agreement(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Convenio'
        verbose_name_plural = 'Convenios'
        ordering = ['name']

    def __str__(self):
        return self.name

# Status model
class Status(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['name']

    def __str__(self):
        return self.name

# Sex model
class Sex(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
        ordering = ['name']

    def __str__(self):
        return self.name

# Training model
class Training(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Formacion'
        verbose_name_plural = 'Formaciones'
        ordering = ['name']

    def __str__(self):
        return self.name

# Employee model
class Employee(models.Model):
    lp = models.CharField(max_length=4, verbose_name="Legajo Personal")
    cuil = models.CharField(max_length=11, verbose_name="CUIL")
    ndoc = models.BigIntegerField(verbose_name="Documento")
    tdoc = models.CharField(max_length=1, verbose_name="Tipo", default="1", choices=DNI_TYPES)
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    calle = models.CharField(max_length=50, verbose_name="Calle")
    numero = models.IntegerField(verbose_name="Número")
    piso = models.IntegerField(verbose_name="Piso")
    unidad = models.CharField(max_length=1, verbose_name="Unidad")
    provincia = models.ForeignKey(Province, null=True, verbose_name="Provincia", on_delete=models.CASCADE)
    localidad = models.ForeignKey(Location, null=True, verbose_name="Localidad", on_delete=models.CASCADE)
    barrio = models.ForeignKey(Neighborhood, null=True, verbose_name="Barrio", on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, null=True, verbose_name="Teléfono")
    celular = models.CharField(max_length=15, null=True, verbose_name="Celular")
    email = models.CharField(max_length=50, null=True, verbose_name="Email")
    foto = models.CharField(max_length=5, null=True, verbose_name="Foto")
    cpost = models.CharField(max_length=5, null=True, verbose_name="Código postal")
    convenio = models.ForeignKey(Agreement, null=True, verbose_name="Convenio", on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contract, null=True, verbose_name="Contrato", on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(Marital, null=True, verbose_name="Estado civil", on_delete=models.CASCADE)
    observaciones = models.TextField(null=True, verbose_name="Observaciones")
    horario = models.CharField(max_length=255, null=True, verbose_name="Horario")
    sexo = models.ForeignKey(Sex, null=True, verbose_name="Sexo", on_delete=models.CASCADE)
    horas_diarias = models.IntegerField(null=True, verbose_name="Horas diarias")
    horas_semanales = models.IntegerField(null=True, verbose_name="Horas semanales")
    horas_mensuales = models.IntegerField(null=True, verbose_name="Horas mensuales")
    sector = models.ManyToManyField(Sector, through="SectorThroughEmployee")
    category = models.ManyToManyField(Category, through="CategoryThroughEmployee")
    destination = models.ManyToManyField(Destination, through="DestinationThroughEmployee")
    charge = models.ManyToManyField(Charge, through="ChargeThroughEmployee")
    photo = models.FileField(null=True, verbose_name="Foto")
    fecha_nacimiento = models.CharField(max_length=10, null=True, verbose_name="Fecha de nacimiento")
    sindicato = models.IntegerField(null=True, verbose_name="Sindicato", default="0", choices=YES_NO)
    obra_social = models.CharField(max_length=255, null=True, verbose_name="Obra social")
    amtedyc = models.IntegerField(null=True, verbose_name="AMTEDyC", default="0", choices=YES_NO)
    temporada = models.IntegerField(null=True, verbose_name="Temporada", default="0", choices=YES_NO)
    cspfa = models.IntegerField(null=True, verbose_name="CSPFA", default="0", choices=YES_NO)
    deportes = models.IntegerField(null=True, verbose_name="Deportes", default="0", choices=YES_NO)
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")
    training = models.ManyToManyField(Training, through="TrainingThroughEmployee")

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['lp']

    def __str__(self):
        return self.lp

# Up model
class Up(models.Model):
    employee = models.ForeignKey(Employee, verbose_name="Empleado", on_delete=models.CASCADE)
    date = models.CharField(max_length=10, null=False, verbose_name="Fecha")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Alta'
        verbose_name_plural = 'Altas'
        ordering = ['date']

    def __str__(self):
        return self.date

# Down Reason model
class DownReason(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Motivo baja'
        verbose_name_plural = 'Motivos baja'
        ordering = ['name']

    def __str__(self):
        return self.name

# Document Type model
class Document(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['name']

    def __str__(self):
        return self.name

# Down model
class Down(models.Model):
    employee = models.ForeignKey(Employee, verbose_name="Empleado", on_delete=models.CASCADE)
    date = models.DateField(null=False, verbose_name="Fecha")
    reason = models.ForeignKey(DownReason, verbose_name="Motivo", on_delete=models.CASCADE)
    number = models.CharField(max_length=4, verbose_name="Número")
    year = models.CharField(max_length=4, verbose_name="Año")
    document = models.ForeignKey(Document, verbose_name="Documento", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Baja'
        verbose_name_plural = 'Bajas'
        ordering = ['date']

    def __str__(self):
        return self.date

class TrainingThroughEmployee(models.Model):
    employee = models.ForeignKey(Employee, verbose_name="Empleado", on_delete=models.CASCADE)
    training = models.ForeignKey(Training, verbose_name="Formación", on_delete=models.CASCADE)
    date = models.CharField(max_length=10, null=True, verbose_name="Fecha")
    complete = models.CharField(max_length=2, null=True, verbose_name="Completo")
    institute = models.CharField(max_length=200, null=True, verbose_name="Institución")
    grade = models.CharField(max_length=200, null=True, verbose_name="Título")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

class SectorThroughEmployee(models.Model):
    employee = models.ForeignKey(Employee, verbose_name="Empleado", on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, verbose_name="Sector", on_delete=models.CASCADE)
    date_from = models.CharField(max_length=10, null=True, verbose_name="Fecha desde")
    date_to = models.CharField(max_length=10, null=True, verbose_name="Fecha hasta")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

class CategoryThroughEmployee(models.Model):
    employee = models.ForeignKey(Employee, verbose_name="Empleado", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE)
    date_from = models.CharField(max_length=10, null=True, verbose_name="Fecha desde")
    date_to = models.CharField(max_length=10, null=True, verbose_name="Fecha hasta")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

class DestinationThroughEmployee(models.Model):
    employee = models.ForeignKey(Employee, verbose_name="Empleado", on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, verbose_name="Destino", on_delete=models.CASCADE)
    date_from = models.CharField(max_length=10, null=True, verbose_name="Fecha desde")
    date_to = models.CharField(max_length=10, null=True, verbose_name="Fecha hasta")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")

class ChargeThroughEmployee(models.Model):
    employee = models.ForeignKey(Employee, verbose_name="Empleado", on_delete=models.CASCADE)
    charge = models.ForeignKey(Charge, verbose_name="Cargo", on_delete=models.CASCADE)
    date_from = models.CharField(max_length=10, null=True, verbose_name="Fecha desde")
    date_to = models.CharField(max_length=10, null=True, verbose_name="Fecha hasta")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name="Actualizado")
