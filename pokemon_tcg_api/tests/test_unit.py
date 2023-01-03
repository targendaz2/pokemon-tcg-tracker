from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from .. import views

class ViewTests(TestCase):
    
    def test_index_includes_name_from_POST(self):
        # Generate the request

        # Submit it to the index view

        # Get the output

        # Check for the name from the POST data
        self.fail()
