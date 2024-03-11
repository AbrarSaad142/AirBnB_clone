#!/usr/bin/python3
"""test amenity model"""
import unittest
from models.amenity import Amenity


class Test_State(unittest.TestCase):
    """unittset for amenity class"""

    def test_object(self):
        """test amenity class"""
        self.amenity = Amenity()

    def test_attribute(self):
        """test attribute for amenity class"""
        self.amenity = Amenity()
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertEqual(self.state.__class__.__name__, "Amenity")

    def test_save(self):
        """test save method"""
        self.amenity = Amenity()
        self.state.save()
        self.assertTrue(self.state, "updated_at")

    def test_str(self):
        """test str method"""
        self.amenity = Amenity()
        s = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                  str(self.amenity.id), self.amenity.__dict__)
        self.assertEqual(print(s), print(self.amenity))


if __name__ == "__main__":
    unittest.main()
