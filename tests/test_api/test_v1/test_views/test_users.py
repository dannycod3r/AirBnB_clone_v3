#!/usr/bin/python3
"""Contains testing documentation for app
"""
from api.v1.views import users
import inspect
import pycodestyle as pstyle
import unittest


class TestUsersDocs(unittest.TestCase):
    """testing the documentation for module"""
    def test_pycodestyle_copliant_app(self):
        """Test module is pycodestyle compliant"""
        codestyle = pstyle.StyleGuide(quiet=True)
        result = codestyle.check_files(['api/v1/views/users.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_app_module_docstring(self):
        """Test for test module docstring"""
        self.assertIsNot(users.__doc__, None,
                         "users.py needs a docstring")
        self.assertTrue(len(users.__doc__) >= 1,
                        "users.py needs a docstring")
