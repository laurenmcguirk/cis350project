class team:
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

    def __init__(self, name):
        self.teamName = name

    def setTeamName(self, name):
        self.teamName = name
    
    def getTeamName(self):
        return self.teamName

    def addWins(self):
        self.wins+=1

    def getWins(self):
        return self.wins
    
    def addLosses(self):
        self.losses+=1
    
    def getLosses(self):
        return self.losses
    
    def getSeed(self):
        return self.seed

    def getRecord(self):
        print(self.teamName + ": " + str(self.wins) + " wins and " + str(self.losses) + " losses")