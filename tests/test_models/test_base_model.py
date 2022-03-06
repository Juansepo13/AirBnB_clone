#!/usr/bin/python3
"""
    This is a module test from BaseModel class and your methods.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel_save(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()

    def test_creation(self):
        '''
            this test validate that creation proccess was correct.
        '''

        self.assertEqual(self.save(), None)
