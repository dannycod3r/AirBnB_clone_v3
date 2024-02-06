#!/usr/bin/python3
"""Contains testing documentation for app
"""
from api.v1.views import cities
import inspect
import pycodestyle as pstyle
import unittest


class TestCitiesDocs(unittest.TestCase):
    """testing the documentation for module"""
    def test_pycodestyle_copliant_app(self):
        """Test module is pycodestyle compliant"""
        codestyle = pstyle.StyleGuide(quiet=True)
        result = codestyle.check_files(['api/v1/views/cities.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_app_module_docstring(self):
        """Test for test module docstring"""
        self.assertIsNot(cities.__doc__, None,
                         "cities.py needs a docstring")
        self.assertTrue(len(cities.__doc__) >= 1,
                        "cities.py needs a docstring")
