from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.chrome.webdriver import WebDriver

from ..models import Datasource, Credential, Card


class FunctionalTests(StaticLiveServerTestCase):

    def test_import_card_data_from_an_api(self):
        # I, an admin, do the following via the Django admin site:

        # Set the Pokémon TCG API as a datasource
        tcg_api = Datasource(
            name="Pokemon TCG API",
            url="https://api.pokemontcg.io/v2/cards")
        tcg_api.save()

        # Add my API key for the Pokémon TCG API
        tcg_api_credential = Credential(
            datasource=tcg_api,
            key="fakekey"
        )
        tcg_api_credential.save()

        # Set the API to load its data into the "Card" model
        tcg_api.model = "Card"
        tcg_api.save()

        # Click a button to execute the data load
        tcg_api.load()

        # Afterwards, I can search for and find at least one "Card" named Pikachu
        pikachu_cards = Card.objects.filter(name__icontains="Pikachu")
        self.assertGreater(pikachu_cards.count(), 0)
