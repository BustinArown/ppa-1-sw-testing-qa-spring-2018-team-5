import unittest
import BMI
from math import isnan


class TestBmi(unittest.TestCase):

    def test_height_conversion(self):
        self.assertEqual(BMI.convert(5, 3), 63)

    def test_calculate_bmi(self):
        self.assertTrue(22.65 <= BMI.calculate_bmi(125, 63) <= 22.75)

    def test_inputtype_conversion(self):
        self.assertRaises(TypeError, BMI.convert("kkkl", "dkls"))

    def test_determine_normal(self):
        self.assertEqual(BMI.determine(22), "Normal weight")

    def test_determine_over(self):
        self.assertEqual(BMI.determine(27), "Overweight")

    def test_determine_under(self):
        self.assertEqual(BMI.determine(12), "Underweight")

    def test_determine_obese(self):
        self.assertEqual(BMI.determine(50), "Obese")

    def test_determine_invalid(self):
        self.assertEqual(BMI.determine(float("NaN")), "Invalid input")

    def test_invalid_inputF(self):
        self.assertTrue(isnan(BMI.bmi('lll', 3, 125)))

    def test_invalid_inputI(self):
        self.assertTrue(isnan(BMI.bmi(5, 'blah', 125)))

    def test_invalid_inputW(self):
        self.assertTrue(isnan(BMI.bmi(5, 3, 'kkk')))

    def test_zero(self):
        self.assertNotEqual(BMI.bmi(0, 0, 125), 0)


if __name__ == '__main__':
    unittest.main()
