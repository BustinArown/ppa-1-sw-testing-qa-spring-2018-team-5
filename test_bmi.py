import unittest
import BMI

class Test_bmi(unittest.TestCase):

    def test_main(self):
        self.assertRaises(ValueError, BMI.main())

    def test_valid_input(self):
        self.assertRaises(ValueError, BMI.bmi(5, 3, 125))

    def test_height_conversion(self):
        self.assertEqual(BMI.convert(5, 3), 63)

    def test_determine(self):
        self.assertEqual(BMI.determine(22), "Normal weight")

    def test_invalid_inputF(self):
        self.assertRaises(ValueError, BMI.bmi('blah', 3, 125))

    def test_invalid_inputI(self):
        self.assertRaises(ValueError, BMI.bmi(5, 'blah', 125))

    def test_invalid_inputW(self):
        self.assertRaises(ValueError, BMI.bmi(5, 3, 'blah'))










if __name__ == '__main__':
    unittest.main()


TestRunner.run()
