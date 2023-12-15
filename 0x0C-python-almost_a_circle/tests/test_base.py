
#!/usr/bin/python3

import unittest
from models.base import Base 

class TestBase(unittest.TestCase):

    # Creating an instance of Base with no arguments should set the id attribute to 1.
    def test_create_instance_with_no_arguments(self):
        b = Base()
        self.assertEqual(b.id, 1)

    # Creating multiple instances of Base with no arguments should set the id attribute to a unique value for each instance.
    def test_create_multiple_instances_with_no_arguments(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    # Creating an instance of Base with an id argument should set the id attribute to the value of the argument.
    def test_create_instance_with_id_argument(self):
        b = Base(5)
        self.assertEqual(b.id, 5)