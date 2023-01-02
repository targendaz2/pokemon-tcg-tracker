from django.db import models

class Datasource(models.Model):
    
    name = models.TextField()
    url = models.URLField()

    def load(self):
        pass

class Credential(models.Model):
    
    name = models.TextField()
    key = models.TextField()


class Card(models.Model):
    
    name = models.TextField()
