from django.db import models

class Pais(models.Model):
    nome = models.CharField(max_length=60)
    sigla = models.CharField(max_length=10)

class Estados(models.Model):
    nome = models.CharField(max_length=75)
    uf = models.CharField(max_length=5)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
class Cidades(models.Model):
    nome = models.CharField(max_length=120)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, max_length=5)

