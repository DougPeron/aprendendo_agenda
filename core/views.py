from django.shortcuts import render

# Create your views here.

def lista_eventos(request):
    return render(request,'agenda.html')