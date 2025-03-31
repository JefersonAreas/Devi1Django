from django.db import models
from django.core.validators import MinLengthValidator

class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name='Full Nome')
    birth_data = models.DateField(verbose_name='Birth Date')
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)],verbose_name='CPF')

   # def __str__(self):
   #     return f"{self.name} ({self.birth_data}-{self.cpf})"