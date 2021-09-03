from django.db import models
from apps.categoria.models import Categoria

class Pregunta(models.Model):
    texto = models.CharField(max_length=150)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    respuesta_1 = models.CharField(max_length=150)
    respuesta_2 = models.CharField(max_length=150)
    correcta = models.CharField(max_length=150)

    def __str__(self):
        return self.texto