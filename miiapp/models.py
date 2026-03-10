from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=5000)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo  # Devuelve el título del post como su representación en cadena
    

class user(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class buscadores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)



# Create your models here.
