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
        self.teams = []
        self.matchups_round1 = []
        self.winners_round1 = []
        self.matchups_round2 = []
        self.final_matchup = None


    def runBracket(self):
        """
        method to run the bracket
        """
        team1 = Team("GVSU", 1)
        team2 = Team("Ferris", 8)
        team3 = Team("MSU", 3)
        team4 = Team("CMU", 6)
        team5 = Team("UofM", 5)
        team6 = Team("Hope", 4)
        team7 = Team("Calvin", 7)
        team8 = Team("GRCC", 2)
        self.teams.extend([team1, team2, team3, team4, team5, team6, team7, team8])

        matchups_round1 = [
            ("Match 1", team1, team8),
            ("Match 2", team4, team5),
            ("Match 3", team3, team6),
            ("Match 4", team2, team7)
        ]
        
        # Simulate first round of matchups
        for match_info in matchups_round1:
            match_name, team1, team2 = match_info
            match = Matchup(match_name)
            match.runMatch(team1, team2)
            self.matchups_round1.append(match)
            self.winners_round1.append(match.getWinner())
        
        # Simulate second round of matchups
        matchups_round2 = [
            ("Match 5", self.winners_round1[0], self.winners_round1[1]),
            ("Match 6", self.winners_round1[2], self.winners_round1[3])
        ]

        for match_info in matchups_round2:
            match_name, team1, team2 = match_info
            match = Matchup(match_name)
            match.runMatch(team1, team2)
            self.matchups_round2.append(match)
            
        # Create final matchup
        final_matchup = Matchup("Final Match")
        final_matchup.runMatch(self.matchups_round2[0].getWinner(), self.matchups_round2[1].getWinner())
        self.final_matchup = final_matchup

        print(final_matchup.getWinner().getTeamName() + " won the bracket!")

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

