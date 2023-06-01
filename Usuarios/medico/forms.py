from django import forms
from .models import medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = medico
        fields = [
            'especialidad',
            'consultorio',
            #'ipsAfiliada',

        ]

        labels = {
            'especialidad': 'Especialidad:',
            'consultorio': 'Consultorio:',
            #'ipsAfiliada': 'Ips Afiliada:',

        }
        widgets = {
            'especialidad': forms.TextInput( attrs={'class': 'form-control fw-bold'}),
            'consultorio': forms.TextInput(attrs={'class': 'form-control'}),
            #'ipsAfiliada': forms.Select(attrs={'class': 'form-select form-control'}),
        }
