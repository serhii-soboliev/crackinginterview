import unittest

from parameterized import parameterized

from dynamic.tasks.text_justification import justify_text, calc_cost_of_text_justification


class TestTextJustification(unittest.TestCase):

    @parameterized.expand([
        ['0',
         ["Geeks", "for", "Geeks", "presents", "word", "wrap", "problem"], 15,
         "Geeks for Geeks\npresents word\nwrap problem"
         ],
        ['1',
         ["Tushar", "Roy", "likes", "to", "code"], 10,
         "Tushar\nRoy likes\nto code"
         ],
        ['2',
         ["This", "is", "an", "example", "of", "text", "justification."], 10,
         "This is an\nexample\nof text\njustification."
         ],
        ['3',
         ["This", "is", "an", "example", "of", "text", "justification."], 16,
         "This is an\nexample of text\njustification.",
         ]
    ])
    def test_text_justification(self, num, words, max_width, justified_text):
        self.assertEqual(justified_text, justify_text(words, max_width),
                         "Justified text for test #{} should be:\n{}\n".format(num, justified_text))


    @parameterized.expand([
        ['0', ["Tushar", "Roy", "likes", "to", "code"], 10, 26],
        ['1', ["Geeks", "for", "Geeks", "presents", "word", "wrap", "problem"], 15, 13],
        ['2', ["This", "is", "an", "example", "of", "text", "justification."], 10, 34],
        ['3', ["This", "is", "an", "example", "of", "text", "justification."], 16, 41]
    ])
    def test_text_justification_cost(self, num, words, max_width, justification_cost):
        self.assertEqual(justification_cost, calc_cost_of_text_justification(words, max_width),
                         "Cost of text justification for test #{} should be:{}\n".format(num, justification_cost))


if __name__ == '__main__':
    unittest.main()
