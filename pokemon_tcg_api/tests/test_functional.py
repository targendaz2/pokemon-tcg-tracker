from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.chrome.webdriver import WebDriver

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


class FunctionalTests(StaticLiveServerTestCase):

    def test_search_for_existing_cards(self):
        # A user navigates to the website.

        # They're presented with a search bar.

        # They enter a Pokémon's name and click "search".

        # They're presented with the number of cards containing that name...

        # ...as well as the first few cards containing that name.

        # The user enters another Pokémon's name and clicks "search".

        # They're presented with the number of cards containing that name...

        # ...as well as the first few cards containing that name.

        # Satisfied, the user leaves the site.
        self.fail()
