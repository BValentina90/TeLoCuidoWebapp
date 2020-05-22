from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from myapp.models import Cuidacoches


def mapa(request):
    template = loader.get_template('mapa.html')
    coordenadas = Cuidacoches.objects.all()
    return render(request, 'mapa.html', {'coordenadas': coordenadas})


def lugarocupado(request):
    template = loader.get_template('lugarocupado.html')
    nombre_lugar_trabajo = request.POST['nombre_lugar_trabajo']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    horario_inicio = request.POST['horario_inicio']
    horario_fin = request.POST['horario_fin']
    codigo = "Usted estaciono en la calle "+ nombre_lugar_trabajo + " la persona que cuida su vehiculo es "+ nombre +" "+ apellido + ".Su cuidacoches estara disponible desde las " + horario_inicio + " Hasta las "+ horario_fin
    return render(request, 'lugarocupado.html', {'codigo': codigo})


def propina(request):
    template = loader.get_template('propina.html')
    return HttpResponse(template.render({}, request))


def calificar(request):
    template = loader.get_template('calificar.html')
    return HttpResponse(template.render({}, request))