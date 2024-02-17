"""
CIS 350 Project - Team Class
Author: Lauren McGuirk
Date: February 2024
"""
from matchClass import Matchup
from teamClass import Team

class Bracket:
    """
    This class runs the whole bracket
    Instance variables:
    bracketName: str - name of the bracket
    """

    def __init__(self, bracketName):
        """
        Constructor
        param matchName: str - name of the match
            Raises: ValueError is value passed in is blank
        """
        if bracketName == '':
            raise ValueError('Name entered cannot be blank!')
        self.bracketName = bracketName

    def runBracket(self):
        """
        method to run the bracket
        """
        team1 = Team("Team 1", 1)
        team2 = Team("Team 2", 8)
        team3 = Team("Team 3", 3)
        team4 = Team("Team 4", 6)
        team5 = Team("Team 5", 5)
        team6 = Team("Team 6", 4)
        team7 = Team("Team 7", 7)
        team8 = Team("Team 8", 2)
        match1 = Matchup("Match 1")
        match1.runMatch(team1, team2)
        match2 = Matchup("Match 2")
        match2.runMatch(team3, team4)
        match3 = Matchup("Match 3")
        match3.runMatch(team5, team6)
        match4 = Matchup("Match 4")
        match4.runMatch(team7, team8)
        match5 = Matchup("Match 5")
        match5.runMatch(match1.getWinner(), match2.getWinner())
        match6 = Matchup("Match 6")
        match6.runMatch(match3.getWinner(), match4.getWinner())
        match7 = Matchup("Match 7")
        match7.runMatch(match5.getWinner(), match6.getWinner())

        print(match7.getWinner().getTeamName() + " won the bracket!")

    def getBracketName(self):
        """
        getter for bracketName attribute
        return: str - bracket name
        """
        return self.bracketName

    def setBracketName(self, name):
        """
        setter for the bracketName attribute
        param name: str - bracket name
        """
        self.bracketName = name

