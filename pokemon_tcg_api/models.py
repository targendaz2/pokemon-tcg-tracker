from django.db import models


class Card(models.Model):

    id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='card_images')

    def __str__(self):
        return self.name
