import unittest
from main import camper_age_input as cai


class FunctionTestCase(unittest.TestCase):
    def test_12_years_to_months(self):
        #12 yearsold should be 144 months
        self.assertEqual(144, cai.convert_to_months(12))


if __name__ == '__main__':
    unittest.main()
