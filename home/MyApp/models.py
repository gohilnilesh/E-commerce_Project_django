from django.db import models
from django.forms import ModelForm

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=70)
    subject = models.TextField(max_length=30)
    message = models.TextField(default="")

    def __str__(self):
        return self.name + "" + self.email
    


