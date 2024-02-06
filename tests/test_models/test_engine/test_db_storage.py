#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pycodestyle as pep8
import sqlalchemy
import unittest
from unittest.mock import MagicMock, patch
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """setup db for test"""
        self.storage = DBStorage()
        self.storage.reload()

    @patch('sqlalchemy.create_engine')
    def test_get_with_valid_class_and_id(self, mock_create_engine):
        """test get method with valid class and id"""
        # Mocking session.query().count() to return a specific count value
        mock_query = MagicMock()
        mock_query.count.return_value = 1
        mock_session = MagicMock()
        mock_session.query().filter_by().first.return_value = "Object"
        mock_session.query().count.return_value = 1
        mock_session.__enter__.return_value = mock_session
        mock_create_engine.return_value = MagicMock()
        mock_create_engine.return_value.__enter__.return_value = mock_session

        # Testing get method with valid class and ID
        result = self.storage.get(Amenity, "123")
        self.assertEqual(result, "Object")

    @patch('sqlalchemy.create_engine')
    def test_get_with_invalid_class(self, mock_create_engine):
        """test with invalid class without id"""
        # Mocking session.query().count() to return a specific count value
        mock_query = MagicMock()
        mock_query.count.return_value = 0
        mock_session = MagicMock()
        mock_session.query().filter_by().first.return_value = None
        mock_session.query().count.return_value = 0
        mock_session.__enter__.return_value = mock_session
        mock_create_engine.return_value = MagicMock()
        mock_create_engine.return_value.__enter__.return_value = mock_session

        # Testing get method with invalid class
        result = self.storage.get("InvalidClass", "123")
        self.assertIsNone(result)

    @patch('sqlalchemy.create_engine')
    def test_count_with_valid_class(self, mock_create_engine):
        """test with invalid class only"""
        # Mocking session.query().count() to return a specific count value
        mock_query = MagicMock()
        mock_query.count.return_value = 2
        mock_session = MagicMock()
        mock_session.query().count.return_value = 2
        mock_session.__enter__.return_value = mock_session
        mock_create_engine.return_value = MagicMock()
        mock_create_engine.return_value.__enter__.return_value = mock_session

        # Testing count method with valid class
        result = self.storage.count(Amenity)
        self.assertEqual(result, 2)

    @patch('sqlalchemy.create_engine')
    def test_count_with_invalid_class(self, mock_create_engine):
        """test count with invalid class"""
        # Mocking session.query().count() to return a specific count value
        mock_query = MagicMock()
        mock_query.count.return_value = 0
        mock_session = MagicMock()
        mock_session.query().count.return_value = 0
        mock_session.__enter__.return_value = mock_session
        mock_create_engine.return_value = MagicMock()
        mock_create_engine.return_value.__enter__.return_value = mock_session

        # Testing count method with invalid class
        result = self.storage.count("InvalidClass")
        self.assertEqual(result, 0)
