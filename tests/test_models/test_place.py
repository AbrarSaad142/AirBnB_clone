#!/usr/bin/python3
"""test place model"""
import unittest
from models.place import Place


class Test_place(unittest.TestCase):
    """unittset for place class"""

    def test_object(self):
        """test place class"""
        self.place = Place()

    def test_attribute(self):
        """test attribute for place class"""
        self.place = Place()
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "random_attr"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "id"))
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_save(self):
        """test save method"""
        self.place = Place()
        self.place.save()
        self.assertTrue(self.place, "updated_at")

    def test_str(self):
        """test str method"""
        self.place = Place()
        s = "[{}] ({}) {}".format(self.place.__class__.__name__,
                                  str(self.place.id), self.place.__dict__)
        self.assertEqual(print(s), print(self.place))


if __name__ == "__main__":
    unittest.main()
