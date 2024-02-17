"""
CIS 350 Project - Team Class
Author: Lauren McGuirk
Date: February 2024
"""
import teamClass
import random

class Matchup:
    """
    This class runs a match in a bracket
    Instance variables:
    matchName: str - name of the match
    firstTeam: team - first team in match
    secondTeam: team - second team in match
    firstScore: int - first team's score
    secondScore: int - second team's score
    winner: str - winner of the match
    loser: str - loser of the match
    """

    firstTeam = ""
    secondTeam = ""
    firstScore = 0
    secondScore = 0
    winner = ""
    loser = ""

    def __init__(self, matchName):
        """
        Constructor
        param matchName: str - name of the match
            Raises: ValueError is value passed in is blank
        """
        if matchName == '':
            raise ValueError('Name entered cannot be blank!')
        self.matchName = matchName

    def runMatch(self, firstTeam, secondTeam):
        """
        method to execute the match
        """
        firstScore = self.randomTeamScore(firstTeam)

        secondScore = self.randomTeamScore(secondTeam)

        #adding to wins/losses of teams
        if firstScore > secondScore:
            print(firstTeam.getTeamName() + " won " + self.getMatchName())
            print("The final score was " + str(firstScore) + " to " + str(secondScore))
            self.setWinner(firstTeam)
            self.setLoser(secondTeam)
        elif secondScore > firstScore:
            print(secondTeam.getTeamName() + " won " + self.getMatchName())
            print("The final score was " + str(secondScore) + " to " + str(firstScore))
            self.setWinner(secondTeam)
            self.setLoser(firstTeam)
    
    def randomTeamScore(self, team):
        """
        method to give each team a random score based on their seed
        """
        score = 0

        if team.getSeed() == 1:
            score = random.randrange(60,100)
        elif team.getSeed() == 2:
            score = random.randrange(45,95)
        elif team.getSeed() == 3:
            score = random.randrage(40,90)
        elif team.getSeed() == 4:
            score = random.randrange(35,85)
        elif team.getSeed() == 5:
            score = random.randrange(30,80)
        elif team.getSeed() == 6:
            score = random.randrange(25,75)
        elif team.getSeed() == 7:
            score = random.randrange(20,70)
        else:
            score = random.randrange(0,65)
        
        return score
    
    
    def getWinner(self):
        """
        getter for winner attribute
        return: int - seed number
        """
        return self.winner

    def setWinner(self, team):
        """
        setter for the winner attribute
        param team: team - winning team
        """
        self.winner = team

    def getLoser(self):
        """
        getter for loser attribute
        return: team - loser of match
        """
        return self.loser
    
    def setLoser(self, team):
        """
        setter for the loser attribute
        param team: team - losing team
        """
        self.loser = team

    def getMatchName(self):
        """
        getter for matchName attribute
        return: str - match name
        """
        return self.matchName

    def setMatchName(self, name):
        """
        setter for the matchName attribute
        param name: str - match name
        """
        self.matchName = name


