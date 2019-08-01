from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Competition(models.Model):
    name = models.CharField(max_length=255)
    pays = models.CharField(max_length=30)
    detail=models.TextField()
    date_add= models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
       return self.name

class Coureur(models.Model):
    nom = models.CharField(max_length=255)
    nationaliter=models.CharField(max_length=30)
    competition =models.ForeignKey('Competition',on_delete=models.CASCADE,related_name="coureur_competition",null = True) 

    def __unicode__(self):
       return self.nom

class utilisateur(models.Model):
    username= models.CharField(max_length=255)
    mail=models.EmailField(max_length=50)
    password= models.CharField(max_length=50)

    def __unicode__(self):
       return self.username



class ticket(models.Model):
    date_ticket= models.DateTimeField(auto_now_add=True)
    choixcoureur=models.ForeignKey('Coureur',on_delete=models.CASCADE,related_name="choix_coureur",null = True)
    mise= models.IntegerField()
    gain=models.IntegerField()

    def __unicode__(self):
       return self.date_ticket
