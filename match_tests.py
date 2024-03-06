import unittest
from matchClass import Matchup, Team 

class TestMatchup(unittest.TestCase):
    def setUp(self):
        # Initialize teams for testing
        self.team1 = Team("Team A", 1)
        self.team2 = Team("Team B", 2)

    def test_match_creation(self):
        # Test match creation with a valid name
        matchup = Matchup("Test Match")
        self.assertEqual(matchup.getMatchName(), "Test Match")

        # Test match creation with an invalid name (blank)
        with self.assertRaises(ValueError):
            Matchup("")

    def test_run_match(self):
        # Test the runMatch method
        matchup = Matchup("Test Match")
        matchup.runMatch(self.team1, self.team2)

        # Ensure the winner and loser are set correctly
        self.assertIsNotNone(matchup.getWinner())
        self.assertIsNotNone(matchup.getLoser())

    def test_random_team_score(self):
        # Test the randomTeamScore method
        matchup = Matchup("Test Match")
        score = matchup.randomTeamScore(self.team1)

        # Ensure the score is within the expected range
        self.assertTrue(0 <= score <= 100)

    def test_getters_and_setters(self):
        # Test getters and setters for various attributes
        matchup = Matchup("Test Match")

        matchup.setWinner(self.team1)
        self.assertEqual(matchup.getWinner(), self.team1)

        matchup.setLoser(self.team2)
        self.assertEqual(matchup.getLoser(), self.team2)

        matchup.setMatchName("New Match Name")
        self.assertEqual(matchup.getMatchName(), "New Match Name")

    

if __name__ == '__main__':
    unittest.main()
