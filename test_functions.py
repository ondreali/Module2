import unittest
from main import camper_age_input as cai


class FunctionTestCase(unittest.TestCase):
    def test_5_years_to_months(self):
        #5 years old should be 60 months
        self.assertEqual(60, cai.convert_to_months(5))


if __name__ == '__main__':
    unittest.main()
