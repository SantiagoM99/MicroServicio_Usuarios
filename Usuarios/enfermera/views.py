from django.http import HttpResponse
from django.shortcuts import render
from .logic import enfermera_logic as hl
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

def enfermeras_list(request):
    enfermeras = hl.get_enfermeras()
    context = {
        'enfermeras_list': enfermeras
        }
    return render(request, 'enfermera/enfermeras.html', context)

def enfermera_detail(request, pk):
    enfermera_dto = hl.get_enfermera(pk)
    enfermera_json = serializers.serialize('json', [enfermera_dto,])
    enfermera = json.loads(enfermera_json)[0]  # extract the first object from the list
    pk_value = enfermera['pk']
    
    return render(request, 'enfermera/enfermera_detail.html', {'enfermera': enfermera, 'pk_value': pk_value})

@csrf_exempt
def enfermeras_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            enfermera_dto = hl.get_enfermera(id)
            enfermera = serializers.serialize('json', [enfermera_dto,])
            return HttpResponse(enfermera, 'application/json')
        else:
            enfermera_dto = hl.get_enfermeras()
            enfermera = serializers.serialize('json', [enfermera_dto,])
            return HttpResponse(enfermera, 'application/json')
    if request.method == 'POST':
        enfermera_dto = hl.create_enfermera(json.loads(request.body))
        enfermera = serializers.serialize('json', [enfermera_dto,])
        return HttpResponse(enfermera, 'application/json')

@csrf_exempt
def enfermera_view(request, pk):
    if request.method == 'GET':
        enfermera_dto = hl.get_enfermera(pk)
        enfermera = serializers.serialize('json', [enfermera_dto,])
        return HttpResponse(enfermera, 'application/json')