from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import random

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

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.chrome_options = Options()
        cls.chrome_options.headless = True
        cls.selenium = WebDriver(options=cls.chrome_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_search_for_existing_cards(self):
        # A user navigates to the website.
        self.selenium.get(self.live_server_url)

        # They pick a Pokémon they want to search for
        names_to_search = random.choices(pokemon_names, k=2)

        # They enter a Pokémon's name into the search bar and click "search".
        search_bar = self.selenium.find_element(
            By.CSS_SELECTOR, 'input[type="text"]')
        search_bar.send_keys(names_to_search[0])
        search_button = self.selenium.find_element(
            By.CSS_SELECTOR, 'input[value="Search"]')
        search_button.click()

        # They're presented with the number of cards containing that name...
        results_count = self.selenium.find_element(
            By.XPATH, "//*[contains(text(),'Results: ')]")

        # ...as well as the first few cards containing that name.
        results = self.selenium.find_elements(
            By.XPATH, f'//*[contains(text(),\'{names_to_search[0]}\')]')
        self.assertGreater(len(results), 0)

        # The user enters another Pokémon's name and clicks "search".
        search_bar = self.selenium.find_element(
            By.CSS_SELECTOR, 'input[type="text"]')
        search_bar.send_keys(names_to_search[1])
        search_button = self.selenium.find_element(
            By.CSS_SELECTOR, 'input[value="Search"]')
        search_button.click()

        # They're presented with the number of cards containing that name...
        results_count = self.selenium.find_element(
            By.XPATH, "//*[contains(text(),'Results: ')]")

        # ...as well as the first few cards containing that name.
        results = self.selenium.find_elements(
            By.XPATH, f'//*[contains(text(),\'{names_to_search[1]}\')]')
        self.assertGreater(len(results), 0)

        # Satisfied, the user leaves the site.
