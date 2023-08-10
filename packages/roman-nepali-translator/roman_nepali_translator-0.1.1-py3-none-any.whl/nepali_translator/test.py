import unittest
from translator import roman_to_unicode_nepali


class TestRomanToNepali(unittest.TestCase):

    def test_single_word_conversion(self):
        roman_text = "hello"
        expected_nepali_text = "नमस्ते"
        self.assertEqual(roman_to_unicode_nepali(
            roman_text), expected_nepali_text)

    # Other test cases...


if __name__ == '__main__':
    unittest.main()
