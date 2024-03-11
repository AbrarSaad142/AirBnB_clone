#!/usr/bin/python3
"""test review model"""
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """unittset for review class"""

    def test_object(self):
        """test review class"""
        self.review = Review()

    def test_attribute(self):
        """test attribute for review class"""
        self.review = Review()
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "random_attr"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertEqual(self.review.text, "")
        self.assertEqual(self.review.__class__.__name__, "Review")

    def test_save(self):
        """test save method"""
        self.review = Review()
        self.state.save()
        self.assertTrue(self.review, "updated_at")

    def test_str(self):
        """test str method"""
        self.review = Review()
        s = "[{}] ({}) {}".format(self.review.__class__.__name__,
                                  str(self.review.id), self.review.__dict__)
        self.assertEqual(print(s), print(self.review))


if __name__ == "__main__":
    unittest.main()
