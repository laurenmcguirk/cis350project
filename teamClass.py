"""
CIS 350 Project - Team Class
Author: Lauren McGuirk
Date: February 2024
"""
class Team:
    """
    This class implements a team in a bracket
    Instance variables:
    teamName: str - name of the team
    wins: int - number of wins the team has in bracket
    losses: int - number of loses the team has in bracket
    seed: int - seed of the team in the bracket
    """
    wins = 0
    losses = 0

    def __init__(self, name, seed):
        """
        Constructor
        param name: str - name of the team
            Raises: ValueError is value passed in is blank
        param seed: int - seed of the team
        """
        if name == '':
            raise ValueError('Names entered cannot be blank!')
        self.teamName = name
        self.seed = seed

    def setTeamName(self, name):
        """
        setter for the teamName attribute
        param teamName: str - the new name for the team
            raises ValueError: if the str passed in is blank
        """
        if name == '':
            raise ValueError('Names entered cannot be blank!')
        self.teamName = name
    
    def getTeamName(self):
        """
        getter for teamName attribute
        return: str - name of the team
        """
        return self.teamName
    
    def getSeed(self):
        """
        getter for seed attribute
        return: int - seed number
        """
        return self.seed

    # def addWins(self):
    #     """
    #     method to add one additional win to the team's win record
    #     """
    #     self.wins+=1

    # def getWins(self):
    #     """
    #     getter for wins attribute
    #     return: int - number of team wins
    #     """
    #     return self.wins
    
    # def addLosses(self):
    #     """
    #     method to add one additional loss to the team's loss record
    #     """
    #     self.losses+=1
    
    # def getLosses(self):
    #     """
    #     getter for losses attribute
    #     return: int - number of team losses
    #     """
    #     return self.losses

    # def getRecord(self):
    #     """
    #     getter for record attribute
    #     return: str - number of team wins vs losses
    #     """
    #     print(self.teamName + ": " + str(self.wins) + " wins and " + str(self.losses) + " losses")
