from..models import medico
#from ips.models import ips

def get_medicos():
    medicos_t = medico.objects.all()
    return medicos_t

def get_medico(medico_pk):
    medico_t = medico.objects.get(pk=medico_pk)
    return medico_t

def create_medico(medico_param):
    medico_pk = ips.objects.get(pk= medico_param['ipsAfiliada'])
    medico_t = medico(
        especialidad = medico_param['especialidad'],
        consultorio = medico_param['consultorio'],
        ipsAfiliada = medico_pk
        )
    medico_t.save()
    return medico_t

def create_medico_form(form):
    medico = form.save()
    medico.save()
    return ()