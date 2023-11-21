from django.db import models

# Create your models here.
"""
class Ejemplo(models.Model o lo que necesites heredar):
    campo1 = models.CharField(verbose_name='Nombre del campo' ,max_length=50)
    campo2 = models.ForeingKey(Para Relacionar Modelos)
    
    class Meta:
        verbose_name = 'Ejemplo'
        verbose_name_plural = 'Ejemplos'
        
    def __str__(self):
        return f'Lo que se vaya a mostrar en el admin'
"""
