#!/usr/bin/python3
"""unit test for base model class"""
import unittest
from models.base_model import BaseModel

my_model = BaseModel()


class TestBaseModwl(unittest.TestCase):
    def test_init(self):
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        old_updated_at = my_model.updated_at
        new_updated_at = my_model.save()
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"],
                         my_model.updated_at.isoformat())

    def test_str(self):
        self.assertTrue(str(my_model).startswith("[BaseModel]"))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

    if __name__ == "__main__":
        unittest.main()
