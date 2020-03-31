from django.db import models
from django.utils import timezone

# Create your models here.

class ModelEstado(models.Model):
   nombre = models.CharField(max_length=254, null=False)
   delete = models.BooleanField(default=False)
   create = models.DateTimeField(default=timezone.now)
   def __str__(self):
      return self.nombre

class ModelCiudad(models.Model):
   nombre = models.CharField(max_length=254, null=False)
   delete = models.BooleanField(default=False)
   create = models.DateTimeField(default=timezone.now)
   def __str__(self):
      return self.nombre

class ModelGenero(models.Model):
   sexo = models.CharField(max_length=254, null=False)
   delete = models.BooleanField(default=False)
   create = models.DateTimeField(default=timezone.now)
   def __str__(self):
      return self.sexo

class ModelOcupacion(models.Model):
   nombre = models.CharField(max_length=254, null=False)
   delete = models.BooleanField(default=False)
   create = models.DateTimeField(default=timezone.now)
   def __str__(self):
      return self.nombre

class ModelEstadoCivil(models.Model):
    estado = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    def __str__(self):
       return self.estado

class Perfil(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apPat = models.CharField(max_length=254,null=False)
    apMat = models.CharField(max_length=254,null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(ModelCiudad,on_delete=models.CASCADE)
    estado = models.ForeignKey(ModelEstado,on_delete=models.CASCADE)
    genero = models.ForeignKey(ModelGenero,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(ModelOcupacion,on_delete=models.CASCADE)
    estadoCivil = models.ForeignKey(ModelEstadoCivil,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre,self.apPat,self.apMat,self.edad
        

    class Meta:
        db_table = 'Perfil'
