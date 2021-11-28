from django.db import models

# Create your models here.

class Futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido =models.CharField(max_length=20)
    edad = models.IntegerField()
    def __str__(self):
        return f'Futbolista {self.nombre} {self.apellido}, Edad: {self.edad}'

class Basquetbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido =models.CharField(max_length=20)
    triples = models.IntegerField()
    def __str__(self):
        return f'Basquetbolista {self.nombre} {self.apellido}, Triples: {self.triples}'
    
class Tenista(models.Model):
    nombre =models.CharField(max_length=20)
    apellido =models.CharField(max_length=20)
    titulos = models.IntegerField()
    def __str__(self):
        return f'Tenista {self.nombre} {self.apellido}, Títulos: {self.titulos}'