from django.db import models

#Modelo de Cuadrilla
class Cuadrilla(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=False,blank=False)

    def __str__(self):
        return self.fecha_creacion


#Modelo de los integrantes
class Integrante(models.Model):
    #Tupla de los tipos de integrantes
    TIPOS_INTEGRANTES = (
        ('1', 'Albañil'),
        ('2', 'Maestro de obra')
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80,null=False, blank=True)
    apellido = models.CharField(max_length=80, null=False, blank=True)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=True)
    tipo = models.CharField(
        max_length=1,
        choices=TIPOS_INTEGRANTES,
        default='1'
    )

    #Llave foranea de la cuadrilla
    cuadrilla = models.ForeignKey('Cuadrilla', null=True)


    def __str__(self):
        return self.nombre

#Modelo de los Familiares
class Familiares(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, null=False, blank=False)
    parentesco = models.CharField(max_length=45, null=False, blank=False)
    telefono = models.CharField(max_length=8, null=False, blank=False)
    #Llave foranea de los integrantes
    integrante = models.ForeignKey('Integrante', null=False, blank=False)
