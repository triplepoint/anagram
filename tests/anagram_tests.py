import unittest
from collections import defaultdict
from anagram.anagram import put_word_in_anagram_dictionary, get_anagrams_from_file


class UnitTests(unittest.TestCase):
    def test_put_word_in_anagram_dictionary(self):
        x = defaultdict(list)

        put_word_in_anagram_dictionary("elvis", x)
        self.assertEqual(x, {
            "eilsv": ["elvis"],
            })

        put_word_in_anagram_dictionary("lives", x)
        self.assertEqual(x, {
            "eilsv": ["elvis", "lives"],
            })

        put_word_in_anagram_dictionary("loves", x)
        self.assertEqual(x, {
            "eilsv": ["elvis", "lives"],
            "elosv": ["loves"],
            })


    def test_get_anagrams_from_file(self):
        a = get_anagrams_from_file("./tests/small_dict", 4)
        self.assertEqual(a, {
            "einrs": ["reins", "resin", "rinse", "risen", "serin", "siren"],
            "einrt": ["inert", "inter", "niter", "retin", "trine"],
            "eimrt": ["merit", "miter", "mitre", "remit", "timer"],
            "eimt":  ["emit", "item", "mite", "time"],
            "einst": ["inset", "neist", "snite", "stein", "stine", "tsine"],
            })

        a = get_anagrams_from_file("./tests/small_dict", 5)
        self.assertEqual(a, {
            "einrs": ["reins", "resin", "rinse", "risen", "serin", "siren"],
            "einrt": ["inert", "inter", "niter", "retin", "trine"],
            "eimrt": ["merit", "miter", "mitre", "remit", "timer"],
            "einst": ["inset", "neist", "snite", "stein", "stine", "tsine"],
            })


if __name__ == '__main__':
    unittest.main()
