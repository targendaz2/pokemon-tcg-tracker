from django.test import TestCase, Client
from django.urls import reverse

import random

from .. import views

pokemon_names = [
    "Bulbasaur",
    "Ivysaur",
    "Venusaur",
    "Charmander",
    "Charmeleon",
    "Charizard",
    "Squirtle",
    "Wartortle",
    "Blastoise",
    "Pikachu",
    "Raichu",
    "Ditto",
    "Eevee",
    "Vaporeon",
    "Jolteon",
    "Flareon",
    "Porygon",
    "Articuno",
    "Zapdos",
    "Moltres",
    "Mewtwo",
    "Chikorita",
    "Bayleef",
    "Meganium",
    "Cyndaquil",
    "Quilava",
    "Typhlosion",
    "Totodile",
    "Croconaw",
    "Feraligatr",
    "Pichu",
    "Espeon",
    "Umbreon",
    "Porygon2",
    "Raiku",
    "Entei",
    "Suicune",
    "Lugia",
    "Ho-Oh"
]

class ViewTests(TestCase):
    
    def test_index_includes_name_from_POST(self):
        client = Client()
        name = random.choice(pokemon_names)

        # Generate the POST data
        post_data = {'name': name}

        # Submit it to the index view
        response = client.post(reverse('index'), post_data)

        # Check the response for the card name
        self.assertContains(response, name)

    def test_index_includes_count_in_context_on_POST(self):
        client = Client()
        name = random.choice(pokemon_names)

        # Generate the POST data
        post_data = {'name': name}

        # Submit it to the index view
        response = client.post(reverse('index'), post_data)

        # Check the response for the card name
        self.assertIsNotNone(response.context['count'])
