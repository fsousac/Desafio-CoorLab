from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Trip(models.Model):
    name = models.CharField(max_length=100)
    price_confort = models.CharField(max_length=15)
    price_econ = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    duration = models.CharField(max_length=3)
    seat = models.CharField(max_length=4, null=True)
    bed = models.CharField(max_length=4, null=True)

    class Meta:
        app_label = 'api'

    def getTrip(self):
        return self.__str__()

    def setName(self, nome):
        self.name = nome
        self.save()

    def setPriceConfort(self, preco):
        self.price_confort = preco
        self.save()

    def setPriceEcon(self, preco):
        self.price_econ = preco
        self.save()

    def setDestino(self, cidade):
        self.cidade_destino = cidade
        self.save()

    def setDuration(self, tempo):
        self.duration = tempo
        self.save()

    def setSeat(self, numero):
        self.seat = numero
        self.save()

    def setBed(self, numero):
        self.bed = numero
        self.save()

    def __str__(self):
        return f'''
    "id": {self.id},                              
    "name": {self.name},           
    "price_confort": {self.price_confort},         
    "price_econ": {self.price_econ},            
    "city": {self.city},                  
    "duration": {self.duration},                    
    "seat": {self.seat},                         
    "bed": {self.bed}    
    '''
