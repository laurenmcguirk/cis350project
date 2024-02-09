"""
CIS 350 Project - Team Class
Author: Lauren McGuirk
Date: February 2024
"""
import teamClass
import random

class Matchup:

    firstTeam = ""
    secondTeam = ""
    firstScore = 0
    secondScore = 0

    def __init__(self, matchName, firstTeam, secondTeam):
        self.matchName = matchName
        self.firstTeam = firstTeam
        self.secondTeam = secondTeam

    def runMatch(self, firstTeam, secondTeam):
        firstScore = self.randomTeamScore(firstTeam)

        secondScore = self.randomTeamScore(secondTeam)

        #adding to wins/losses of teams
        if firstScore > secondScore:
            print(firstTeam.getTeamName() + " won the match!")
            print("The final score was " + str(firstScore) + " to " + str(secondScore))
            self.firstTeam.addWins() 
            self.secondTeam.addLosses()
            self.setWinner(firstTeam)
            self.setLoser(secondTeam)
        elif secondScore > firstScore:
            print(secondTeam.getTeamName() + " won the match!")
            print("The final score was " + str(secondScore) + " to " + str(firstScore))
            self.secondTeam.addWins()
            self.firstTeam.addLosses()
            self.setWinner(secondTeam)
            self.setLoser(firstTeam)
    
    def randomTeamScore(self, team):
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
        return self.winner

    def setWinner(self, team):
        self.winner = team

    def getLoser(self):
        return self.loser
    
    def setLoser(self, team):
        self.loser = team

    def getMatchName(self):
        return self.matchName

    def setMatchName(self, name):
        self.matchName = name


