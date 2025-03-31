from django.db import models
from .person import Person

class Passport(models.Model):
    number = models.CharField(max_length=10, verbose_name='Number')
    issue_date = models.DateField(verbose_name='Issue date')
    expiration_date = models.DateField(verbose_name='Expiration Date')
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

   # def __str__(self):
   #     return f"{self.number} ({self.issue_date}-{self.expiration_date})


        
