from django.db import models

# Create your models here.

class Tarea(models.Model):
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)


class SubTarea(models.Model):
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='subtareas')
    descripcion = models.CharField(max_length=255)
    eliminada = models.BooleanField(default=False)