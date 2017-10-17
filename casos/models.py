from django.db import models

class Caso(models.Model):

    TIPOS_PROYECTOS = (
        ('1', 'Mantenimiento'),
        ('2', 'Infraestructura')
    )

    ESTADOS = (
        ('1', 'Ejecutando'),
        ('2', 'Terminado')
    )

    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_final = models.DateField(null=False, blank=True)
    nombre = models.CharField(max_length=80, null=False, blank=False)
    # Para obtener la cadena de esta campo, se llama al
    # metodo <objeto>.get_tipo_display()
    tipo = models.CharField(
        max_length=1,
        choices=TIPOS_PROYECTOS,
        default='1'
    )
    descripcion = models.TextField(max_length=200, null=False, blank=True)
    direccion = models.TextField(max_length=200, null=False, blank=True)
    estado = models.CharField(
        max_length=1,
        choices=ESTADOS,
        default='1'
    )
    #Relación uno a muchos, un caso puede tener muchas tareas
    tareas = models.ManyToManyField('Tarea', related_query_name='tareas')

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    ESTADOS = (
        ('1', 'Ejecutando'),
        ('2', 'Terminado')
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False, blank=False)
    duracion = models.IntegerField(null=True)
    estado = models.CharField(
        max_length=1,
        choices=ESTADOS,
        default='1'
    )

    def __str__(self):
        return self.nombre
