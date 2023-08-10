import unittest

from translator import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()

    def test_conversion(self):
        test_cases = [
            ('gaahro', 'गाह्रो'),
            ('phone number 98432', 'फोन नम्बर ९८४३२'),
            ('aaNNkhaa', 'आँखा'),
        ]

        for roman, nepali in test_cases:
            self.assertEqual(self.converter.convert(roman), nepali)


if __name__ == '__main__':
    unittest.main()
