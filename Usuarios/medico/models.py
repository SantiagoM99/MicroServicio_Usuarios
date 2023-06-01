from django.db import models
#from ips.models import ips

class medico(models.Model):
    especialidad = models.TextField(max_length=50)
    consultorio = models.TextField(max_length=50)
    #ipsAfiliada = models.ForeignKey(ips, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return '{}'.format(self.especialidad,self.consultorio)