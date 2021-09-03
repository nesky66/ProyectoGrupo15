from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.categoria.models import Categoria
from apps.usuarios.models import Usuario
from apps.preguntas.models import Pregunta
from .models import Juego
from django.db.models.aggregates import Count
from random import randint, shuffle







@login_required
def pagJuego(request):
    return render(request,'juego/jugar.html')

def seleccionaJuego(request,op):

    context = {}

    context['intent'] = 5
    context['puntuac'] = 0

    if op==1:
        context['op'] = op
        cat = Categoria.objects.all()
        context['categorias'] = cat
        return render(request,'juego/muestraCategorias.html',context)

    if op == 2:
        context['op'] = op  
        # indice = randomCat() 
        # cat = Categoria.objects.get(id=indice)


    
        # context['categoria'] =  cat

        return render(request,'juego/muestraCategorias.html',context)



def leeBase(categoria):
      
        context={}

        # SELECCIONO UNA PREGUNTA ALAZAR DEL GRUPO DE CATEGORIAS SOLICITADO
        cate = Pregunta.objects.filter(id_categoria=categoria)
        longit = len(cate)
        index = randint(0,longit-1)
        pregunta = cate[index]
        # CARGO LA PREGUNTA Y SUS RESPUESTAS EN UNA LISTA
        correcta = pregunta.correcta
        respuestas = [pregunta.respuesta_1,pregunta.respuesta_2,pregunta.correcta]

        shuffle(respuestas)

        context['correcta'] = correcta
        context['pregunta'] = pregunta.texto
        context['respuestas'] = respuestas
        context['catNom'] = Categoria.objects.get(id=categoria)
        
       
        return context
def randomCat():
    cat = Categoria.objects.all()
    longit = len(cat)

    index = randint(1,longit)
    return index



def juegaCategoria(request,op,cat,pun,inte):

    

    if op == 2:

        cat = randomCat()  

    context = leeBase(cat)
    context['op'] = op
    context['intent'] = inte
    context['puntuc'] = pun


    return render(request,'juego/juegaCategoria.html',context)

def validar(request,op,cat,selec,pregunta,itos,ptos):

   
    context = {}

    if selec == pregunta:
        ptos = ptos + 10
    else:
        
        
        itos = itos - 1

    if itos < 0:
        context['puntos']= ptos
        return render(request,'juego/finJuego.html',context)
    else:
        context = leeBase(cat)
        context['op'] = op
        context['intent'] = itos
        context['puntuc'] = ptos

    # return render(request,'juego/juegaCategoria.html',context)

        return juegaCategoria(request,op,cat,ptos,itos)


