import unittest
from practic1 import (
    reverse_words,
    get_even_numbers,
    categorize_number,
    apply_operation,
    count_char_frequencies
)

class TestLists(unittest.TestCase):
    def test_get_even_numbers_mixed(self):
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
    
    def test_get_even_numbers_all_odd(self):
        self.assertEqual(get_even_numbers([1, 3, 5]), [])
    
    def test_get_even_numbers_empty(self):
        self.assertEqual(get_even_numbers([]), [])

class TestConditions(unittest.TestCase):
    def test_positive_even(self):
        self.assertEqual(categorize_number(8), "positive even")
    
    def test_positive_odd(self):
        self.assertEqual(categorize_number(7), "positive odd")
    
    def test_negative(self):
        self.assertEqual(categorize_number(-5), "negative")
        self.assertEqual(categorize_number(-2), "negative")
    
    def test_zero(self):
        self.assertEqual(categorize_number(0), "zero")

class TestFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(apply_operation(3, 5, "+"), 8)
    
    def test_subtraction(self):
        self.assertEqual(apply_operation(10, 4, "-"), 6)
    
    def test_multiplication(self):
        self.assertEqual(apply_operation(2, 3, "*"), 6)
    
    def test_division(self):
        self.assertAlmostEqual(apply_operation(7, 2, "/"), 3.5)
    
    def test_division_by_zero(self):
        self.assertIsNone(apply_operation(5, 0, "/"))
    
    def test_invalid_operation(self):
        self.assertIsNone(apply_operation(1, 2, "**"))


class TestStrings(unittest.TestCase):
    def test_reverse_words_normal(self):
        self.assertEqual(reverse_words("hello world"), "olleh dlrow")
    
    def test_reverse_words_single_word(self):
        self.assertEqual(reverse_words("Python"), "nohtyP")
    
    def test_reverse_words_empty(self):
        self.assertEqual(reverse_words(""), "")
        
class TestDictionaries(unittest.TestCase):
    def test_count_char_frequencies_simple(self):
        self.assertEqual(count_char_frequencies("aab"), {'a': 2, 'b': 1})
    
    def test_count_char_frequencies_case_sensitive(self):
        self.assertEqual(count_char_frequencies("Aa"), {'A': 1, 'a': 1})
    
    def test_count_char_frequencies_with_space(self):
        self.assertEqual(count_char_frequencies("a a"), {'a': 2, ' ': 1})
    
    def test_count_char_frequencies_empty(self):
        self.assertEqual(count_char_frequencies(""), {})

if __name__ == '__main__':
    unittest.main()