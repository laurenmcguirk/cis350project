import teamClass
import matchClass

# Define teams
team = teamClass.team
team1 = team("Team 1")
team2 = team("Team 2")
team3 = team("Team 3")
team4 = team("Team 4")
team5 = team("Team 5")
team6 = team("Team 6")
team7 = team("Team 7")
team8 = team("Team 8")

# Put teams into matches
match = matchClass.match
match1 = match(team1, team2)
match2 = match(team3, team4)
match3 = match(team5, team6)
match4 = match(team7, team8)