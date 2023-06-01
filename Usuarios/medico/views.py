import json
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .logic import medico_logic as ml
from .forms import MedicoForm

def medicos_list(request):
    medicos = ml.get_medicos()
    context = {
        'medicos_list': medicos
        }
    return render(request, 'Medico/medicos.html', context)

"""
def medico_detail(request, pk):
    medico_dto = ml.get_medico(pk)
    medico_json = serializers.serialize('json', [medico_dto,])
    medico = json.loads(medico_json)[0]  # extract the first object from the list
    pk_value = medico['pk']
    
    return render(request, 'medico/medico_detail.html', {'medico': medico, 'pk_value': pk_value})
"""

@csrf_exempt
def medicos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            medico_dto = ml.get_medico(id)
            medico = serializers.serialize('json', [medico_dto,])
            return HttpResponse(medico, 'application/json')
        else:
            medico_dto = ml.get_medicos()
            medico = serializers.serialize('json', [medico_dto,])
            return HttpResponse(medico, 'application/json')
    if request.method == 'POST':
        medico_dto = ml.create_medico(json.loads(request.body))
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')
@csrf_exempt
def medico_create(request):
        if request.method == 'POST':
            form = MedicoForm(request.POST)
            if form.is_valid():
                ml.create_medico_form(form)
                messages.add_message(request, messages.SUCCESS, 'Medico creado correctamente')
                return HttpResponseRedirect(reverse('createMedico'))
            else:
                print("Fallo al crear medico")
        else:
            form = MedicoForm()

        context = {
            'form': form
        }
        return render(request, 'Medico/createMedico.html', context)

@csrf_exempt
def medico_view(request, pk):
    if request.method == 'GET':
        medico_dto = ml.get_medico(pk)
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')
    if request.method == 'PUT':
        medico_dto = ml.update_medico(pk, json.loads(request.body))
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')


