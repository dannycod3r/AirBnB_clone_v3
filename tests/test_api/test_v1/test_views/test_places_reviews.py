#!/usr/bin/python3
"""Contains testing documentation for app
"""
from api.v1.views import places_reviews
import inspect
import pycodestyle as pstyle
import unittest


class TestPlaceReviewDocs(unittest.TestCase):
    """testing the documentation for module"""
    def test_pycodestyle_copliant_app(self):
        """Test module is pycodestyle compliant"""
        codestyle = pstyle.StyleGuide(quiet=True)
        result = codestyle.check_files(['api/v1/views/places_reviews.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_app_module_docstring(self):
        """Test for test module docstring"""
        self.assertIsNot(places_reviews.__doc__, None,
                         "places_reviews.py needs a docstring")
        self.assertTrue(len(places_reviews.__doc__) >= 1,
                        "places_reviews.py needs a docstring")
