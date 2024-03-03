#!/usr/bin/python3
"""The Module for Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """add and Defines attributes for the Review class"""
    place_id = ""
    user_id = ""
    text = ""
