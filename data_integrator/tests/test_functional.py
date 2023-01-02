from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.chrome.webdriver import WebDriver

import random

from ..models import Datasource, Credential, Card


class FunctionalTests(StaticLiveServerTestCase):

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

    def test_import_card_data_from_an_api(self):
        # I, an admin, do the following via the Django admin site:

        # Set the Pokémon TCG API as a datasource
        tcg_api = Datasource(
            name="Pokémon TCG API",
            url="https://api.pokemontcg.io/v2/cards")
        tcg_api.save()

        # Add my API key for the Pokémon TCG API
        tcg_api_credential = Credential(
            name="Pokémon TCG API Credential",
            key="fakekey"
        )
        tcg_api_credential.save()

        # Link my API key to the Datasource I created
        tcg_api.credential = tcg_api_credential
        tcg_api.save()

        # Set the API to load its data into the "Card" model
        tcg_api.model = "Card"
        tcg_api.save()

        # Click a button to execute the data load
        tcg_api.load()

        # Afterwards...

        # If I search for 3 cards by Pokémon name, I can find at least 1 of each
        for name in random.choices(self.pokemon_names, k=3):
            print(f'Searching for cards named "{name}"...')
            cards = Card.objects.filter(name__icontains=name)
            count = cards.count()
            self.assertGreater(count, 0)
            print(f'Found count cards')
