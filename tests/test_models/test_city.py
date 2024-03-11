#!/usr/bin/python3
"""test city model"""
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """unittset for city class"""

    def test_object(self):
        """test city class"""
        self.city = City()

    def test_attribute(self):
        """test attribute for city class"""
        self.city = City()
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "random_attr"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        self.city.name = "WonderLand"
        self.city.state_id = "Won67L0nd"
        self.assertEqual(self.city.name, "WonderLand")
        self.assertEqual(self.city.state_id, "Won67L0nd")
        self.assertEqual(self.city.__class__.__name__, "City")

    def test_save(self):
        """test save method"""
        self.city = City()
        self.state.save()
        self.assertTrue(self.state, "updated_at")

    def test_str(self):
        """test str method"""
        self.city = City()
        s = "[{}] ({}) {}".format(self.city.__class__.__name__,
                                  str(self.city.id), self.city.__dict__)
        self.assertEqual(print(s), print(self.city))


if __name__ == "__main__":
    unittest.main()
