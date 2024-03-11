#!/usr/bin/python3
"""Defines user test model
"""
import os
import models
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """test the User class."""
    def setUpClass(cls):
        cls.myUser = User()
        cls.myUser.first_name = "Abrar"
        cls.myUser.last_name = "Saad"
        cls.myUser.email = "abrarsaad917@gmail.com"
        cls.myUser.password = "root"

    def tearDown(cls):
        del cls.myUser
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subClass(self):
        """test is a subClass"""
        self.assertTrue(issubclass(self.myUser.__class__, BaseModel), True)

    def test_checkFunction(self):
        """check fn"""
        self.assertIsNotNone(User.__doc__)

    def test_attribute(self):
        """test that class has attribute"""
        self.assertTrue('email' in self.myUser.__dict__)
        self.assertTrue('id' in self.myUser.__dict__)
        self.assertTrue('created_at' in self.myUser.__dict__)
        self.assertTrue('updated_at' in self.myUser.__dict__)
        self.assertTrue('password' in self.myUser.__dict__)
        self.assertTrue('first_name' in self.myUser.__dict__)
        self.assertTrue('last_name' in self.myUser.__dict__)

    def test_attribute_type(self):
        """test typr of attribute"""
        self.assertEqual(type(self.myUser.email), str)
        self.assertEqual(type(self.myUser.password), str)
        self.assertEqual(type(self.myUser.first_name), str)
        self.assertEqual(type(self.myUser.last_name), str)

    def test_save(self):
        """test save method"""
        self.myUser.save()
        self.assertNotEqual(self.myUser.crereated_at, self.myUser.updated_at)

    def test_to_dict(self):
        """test to_dict method"""
        self.assertEqual('to-dict' in dir(self.myUser), True)


if __name__ == "__main__":
    unittest.main()
