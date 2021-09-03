from django.urls import path, include
from . import views

app_name='juego'

urlpatterns = [
    path('jugar/', views.pagJuego, name='jugar'),
    path('jugar2/<int:op>', views.seleccionaJuego, name='selecjuego'),
    path('jugarCat/<int:op>/<int:cat>/<int:pun>/<int:inte>', views.juegaCategoria, name='juegacat'),
    path('valida/<int:op>/<int:cat>/<selec>/<pregunta>/<int:itos>/<int:ptos>', views.validar, name='validar'),
]