from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tarea(models.Model):
    usuario = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True)
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(null=True,
                                   blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
