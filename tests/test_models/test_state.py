#!/usr/bin/python3
"""test review model"""
import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """unittset for state class"""

    def test_object(self):
        """test state class"""
        self.state = State()

    def test_attribute(self):
        """test attribute for state class"""
        self.state = State()
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "random_attr"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertEqual(self.state.name, "")
        self.state.name = "WonderLand"
        self.assertEqual(self.state.name, "WonderLand")
        self.assertEqual(self.state.__class__.__name__, "State")

    def test_save(self):
        """test save method"""
        self.state = State()
        self.state.save()
        self.assertTrue(self.state, "updated_at")

    def test_str(self):
        """test str method"""
        self.state = State()
        s = "[{}] ({}) {}".format(self.state.__class__.__name__,
                                  str(self.state.id), self.state.__dict__)
        self.assertEqual(print(s), print(self.state))


if __name__ == "__main__":
    unittest.main()
