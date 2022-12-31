from django.db import models

class Datasource(models.Model):
    
    name = models.TextField()
    url = models.URLField()

    def load(self):
        pass

class Credential(models.Model):
    
    datasource = models.ForeignKey(Datasource, on_delete=models.CASCADE)
    key = models.TextField()


class Card(models.Model):
    
    name = models.TextField()
