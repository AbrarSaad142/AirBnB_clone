#!/usr/bin/python3
"""User modrl"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class inherts from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
