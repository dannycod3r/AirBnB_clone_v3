#!/usr/bin/python3
"""Contains testing documentation for app
"""
from api.v1 import app
import inspect
import pycodestyle as pstyle
import unittest


class TestAppDocs(unittest.TestCase):
    """testing the documentation for app"""
    def test_pycodestyle_copliant_app(self):
        """Test is app module is pycodestyle compliant"""
        codestyle = pstyle.StyleGuide(quiet=True)
        result = codestyle.check_files(['api/v1/app.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_copliant_test_app(self):
        """Test is app module is pycodestyle compliant"""
        codestyle = pstyle.StyleGuide(quiet=True)
        result = codestyle.check_files(['tests/test_api/test_v1/test_app.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_app_module_docstring(self):
        """Test for the module docstring"""
        self.assertIsNot(app.__doc__, None,
                         "app.py needs a docstring")
        self.assertTrue(len(app.__doc__) >= 1,
                        "app.py needs a docstring")
