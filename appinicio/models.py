from django.db import models

class Auto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    anio = models.IntegerField(default=2010)
    imgauto = models.ImageField(upload_to='imgauto', blank=True, null=True)
    
    
    def __str__(self):
        return f'Auto {self.marca} {self.modelo}'