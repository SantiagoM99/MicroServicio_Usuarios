from..models import enfermera

def get_enfermeras():
    enfermeraes_t = enfermera.objects.all()
    return enfermeraes_t

def get_enfermera(enfermera_pk):
    enfermera_t = enfermera.objects.get(pk=enfermera_pk)
    return enfermera_t

def create_enfermera(enfermera):
    enfermera_t = enfermera.objects.create(
        nombre = enfermera['nombre'],
        nit = enfermera['nit'],
        )
    return enfermera_t