from django.db import models
import os


class Contact(models.Model):
    name = models.CharField( max_length = 100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(default='')

    def __str__(self):
        return self.name












