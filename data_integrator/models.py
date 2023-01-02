from django.db import models

class Datasource(models.Model):
    
    name = models.CharField(max_length=80)
    url = models.URLField()
    last_response = models.JSONField(null=True, blank=True)

    def load(self):
        self.last_response = {"url": "https://api.pokemontcg.io/v2/cards"}
        self.save()

class Credential(models.Model):
    
    name = models.CharField(max_length=80)
    key = models.CharField(max_length=120)


class Card(models.Model):
    
    name = models.CharField(max_length=50)
