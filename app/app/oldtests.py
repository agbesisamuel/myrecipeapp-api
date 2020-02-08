from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that add two numbers"""
        self.assertEqual(add(10, 7), 17)

    def test_subtract_numbers(self):
        """Test that numbers are subtracted"""
        self.assertEqual(subtract(7, 10), 3)
