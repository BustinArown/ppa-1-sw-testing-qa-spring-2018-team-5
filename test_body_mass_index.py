import unittest
from body_mass_index import *


class TestBmi(unittest.TestCase):

    def test_height_conversion(self):
        self.assertEqual(convert(5, 3), 63)

    def test_calculate_bmi(self):
        self.assertTrue(22.65 <= calculate_bmi(125, 63) <= 22.75)

    def test_zero_height_bmi(self):
        self.assertTrue(isnan(calculate_bmi(50, 0)))

    def test_input_type_conversion(self):
        self.assertRaises(TypeError, convert("kkkl", "dkls"))

    def test_determine_normal(self):
        value, string = determine(22)
        self.assertEqual(value, 22)
        self.assertEqual(string, "Normal weight")

    def test_determine_over(self):
        value, string = determine(27)
        self.assertEqual(value, 27)
        self.assertEqual(string, "Overweight")

    def test_determine_under(self):
        value, string = determine(12)
        self.assertEqual(value, 12)
        self.assertEqual(string, "Underweight")

    def test_determine_obese(self):
        value, string = determine(50)
        self.assertEqual(value, 50)
        self.assertEqual(string, "Obese")

    def test_determine_invalid_height(self):
        value, string = determine(float("NaN"))
        self.assertTrue(isnan(value))
        self.assertEqual(string, "Height cannot be zero")

    def test_zero(self):
        self.assertNotEqual(body_mass_index(0, 0, 125), 0)


if __name__ == '__main__':
    unittest.main()
