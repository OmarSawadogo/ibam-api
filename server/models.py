from django.db import models

# Create your models here.

class Cours(models.Model):
    ens = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    matiere = models.CharField(max_length=100)
    vh = models.CharField(max_length=100)

    def __str___(self):
        return self.ens