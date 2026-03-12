from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class post(models.Model):
    class State(models.TextChoices):
        DRAFT = 'D', 'Draft'
        POSTED = 'P', 'Posted'
    title = models.CharField(max_length=50)
    content = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=1,choices=State.choices, default=State.DRAFT)
    class type (models.TextChoices):
        Predatory = 'PD', "Predatory"
        Benevolent = 'BV', 'Benevolent'
        Aquatic = 'AQ', 'Aquatic'
        Undefined = 'U', 'Undefined'
    type = models.CharField(max_length=2,choices=type.choices, default=type.Undefined)

   

    def __str__(self):
        return self.title  # Devuelve el título del post como su representación en cadena
    

class user(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
class cathegory(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=330, unique=True)
    Indexofviolence = models.TextField(null=True, blank=True)





# Create your models here.
