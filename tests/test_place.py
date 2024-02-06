#!/usr/bin/python3
"""
TestPlaceDocs classes
"""
import json
import unittest
import pep8
from flask import Flask
from flask.testing import FlaskClient
from api.v1.views import app_views
from models import storage
from models.place import Place


class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Flask application
        cls.app = Flask(__name__)
        cls.app.register_blueprint(app_views)
        cls.app.config['TESTING'] = True
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        # Clean up after the tests
        storage.close()

    def test_pep8_conformance(self):
        # Check PEP8 conformance using pep8 module
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['api/v1/views.py', 'models/place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

    def test_get_places_by_city(self):
        # Create a city and places for testing
        city = City(name="Test City")
        storage.new(city)
        place1 = Place(name="Place 1", city_id=city.id)
        place2 = Place(name="Place 2", city_id=city.id)
        storage.new(place1)
        storage.new(place2)
        storage.save()

        # Send a GET request to the API endpoint
        response = self.client.get(f'/cities/{city.id}/places')

        # Check the response status code and data
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], "Place 1")
        self.assertEqual(data[1]['name'], "Place 2")

    def test_get_place(self):
        # Create a place for testing
        place = Place(name="Test Place")
        storage.new(place)
        storage.save()

        # Send a GET request to the API endpoint
        response = self.client.get(f'/places/{place.id}')

        # Check the response status code and data
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], "Test Place")


if __name__ == '__main__':
    unittest.main()
