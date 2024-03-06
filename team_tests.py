import unittest
from teamClass import Team

class TestTeamClass(unittest.TestCase):

    def test_constructor_with_valid_input(self):
        team = Team("TeamA", 1)
        self.assertEqual(team.getTeamName(), "TeamA")
        self.assertEqual(team.getSeed(), 1)


    def test_constructor_with_blank_name(self):
        with self.assertRaises(ValueError):
            team = Team("", 1)


    def test_set_team_name_with_valid_input(self):
        team = Team("TeamA", 1)
        team.setTeamName("NewTeamA")
        self.assertEqual(team.getTeamName(), "NewTeamA")


    def test_set_team_name_with_blank_name(self):
        team = Team("TeamA", 1)
        with self.assertRaises(ValueError):
            team.setTeamName("")

   def test_getSeed(self):
        team = Team("TeamA", 1)
        self.assertEqual(team.getSeed(), 1)


if __name__ == '__main__':
    unittest.main()
