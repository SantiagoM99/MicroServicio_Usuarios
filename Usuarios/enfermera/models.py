from django.db import models

class enfermera(models.Model):
    especialidad = models.TextField(max_length=50)
    def __str__(self):
        return '{}'.format(self.especialidad)
