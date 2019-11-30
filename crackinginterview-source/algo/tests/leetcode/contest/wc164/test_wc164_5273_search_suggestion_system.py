import unittest

from parameterized import parameterized

from leetcode.contest.wc164.wc164_5273_search_suggestion_system import SearchSuggestionSystem


class TestSearchSuggestionSystem(unittest.TestCase):

    @parameterized.expand([
        ['0', ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse",
         [
             ["mobile", "moneypot", "monitor"],
             ["mobile", "moneypot", "monitor"],
             ["mouse", "mousepad"],
             ["mouse", "mousepad"],
             ["mouse", "mousepad"]
         ]
         ],
        [
            '1', ["havana"], "havana",
            [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
        ],
        [
            '2', ["bags", "baggage", "banner", "box", "cloths"], "bags",
            [["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]]
        ],
        [
            '3', ["havana"], "tatiana", [[], [], [], [], [], [], []]
        ]

    ])
    def test_search_suggestion_system(self, name, products, search_word, expected):
        self.assertEqual(expected,
                         SearchSuggestionSystem().suggested_products(products, search_word),
                         "Suggestion # {} should be {}".format(name, expected)
                         )
