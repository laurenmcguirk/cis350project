import unittest
from bracketClass import Bracket

class TestBracket(unittest.TestCase):

    def test_init_with_blank_name(self):
        with self.assertRaises(ValueError):
            Bracket('')

    def test_run_bracket(self):
        bracket = Bracket('TestBracket')
        bracket.runBracket()
        # Add assertions based on the expected behavior of the runBracket method

    def test_get_bracket_name(self):
        bracket = Bracket('TestBracket')
        self.assertEqual(bracket.getBracketName(), 'TestBracket')

    def test_set_bracket_name(self):
        bracket = Bracket('TestBracket')
        bracket.setBracketName('NewBracketName')
        self.assertEqual(bracket.getBracketName(), 'NewBracketName')

if __name__ == '__main__':
    unittest.main()
    
