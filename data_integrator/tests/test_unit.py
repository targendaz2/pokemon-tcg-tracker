from django.test import TestCase

from ..models import Datasource, Card

class DatasourceLoadTests(TestCase):
    
    def test_load_method_sends_a_request_to_specified_url(self):
        # Set up test Datasource
        datasource = Datasource(
            name="Test Datasource",
            url="https://api.pokemontcg.io/v2/cards"
        )
        datasource.full_clean()
        datasource.save()

        # Load method is called
        datasource.load()

        # Check the response
        self.assertEqual(datasource.last_response["url"], datasource.url)
