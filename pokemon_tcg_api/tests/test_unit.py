from django.db.models.query import QuerySet
from django.test import TestCase, Client
from django.urls import reverse

import random

from ..models import Card
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

        # Check the response context for the count
        self.assertIsNotNone(response.context['count'])

    def test_index_includes_cards_in_context_on_POST(self):
        client = Client()
        name = random.choice(pokemon_names)

        # Generate the POST data
        post_data = {'name': name}

        # Submit it to the index view
        response = client.post(reverse('index'), post_data)

        # Check the response context for the list
        self.assertIsInstance(response.context['cards'], QuerySet)
        self.assertGreater(len(response.context['cards']), 0)

    def test_index_populates_Cards_on_POST(self):
        client = Client()
        name = random.choice(pokemon_names)

        # Generate the POST data
        post_data = {'name': name}

        # Submit it to the index view
        response = client.post(reverse('index'), post_data)

        # Check the number of Card objects
        self.assertGreater(Card.objects.count(), 0)

    def test_index_merges_duplicate_Cards_on_POST(self):
        client = Client()
        name = random.choice(pokemon_names)

        # Generate the POST data
        post_data = {'name': name}

        # Submit it to the index view
        client.post(reverse('index'), post_data)

        # Check the number of Card objects
        initial_card_count = Card.objects.count()

        # POST to the index view once more
        client.post(reverse('index'), post_data)

        # Check that the number of Card objects has not changed
        self.assertEqual(initial_card_count, Card.objects.count())
