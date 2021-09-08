from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def registerUser(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado con exito')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context={'form': form }
    return render(request,'usuarios/register.html',context)
