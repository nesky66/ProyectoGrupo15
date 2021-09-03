from django.db import models
from django.db.models.deletion import SET_NULL
from apps.usuarios.models import Usuario

class Juego(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)
    cantidad_correctas = models.IntegerField(default=0)

    def __str__(self):
        return self.id_usuario