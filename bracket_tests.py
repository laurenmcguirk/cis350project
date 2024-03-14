import unittest
from matchClass import Matchup
from teamClass import Team
from bracketClass import Bracket  

class TestBracket(unittest.TestCase):

    def test_bracket_creation_valid_name(self):
        bracket = Bracket("Test Bracket")
        self.assertEqual(bracket.getBracketName(), "Test Bracket")

    def test_bracket_creation_blank_name(self):
        with self.assertRaises(ValueError):
            Bracket("")

    def test_run_bracket(self):
        bracket = Bracket("Test Bracket")
        bracket.runBracket()  # checking if the method runs without errors

    def test_get_bracket_name(self):
        bracket = Bracket("Test Bracket")
        self.assertEqual(bracket.getBracketName(), "Test Bracket")

    def test_set_bracket_name(self):
        bracket = Bracket("Test Bracket")
        bracket.setBracketName("New Bracket Name")
        self.assertEqual(bracket.getBracketName(), "New Bracket Name")

if __name__ == '__main__':
    unittest.main()

    
