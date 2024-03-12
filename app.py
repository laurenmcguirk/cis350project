from flask import Flask, jsonify
from bracketClass import Bracket


# This file replaced main.py
# This does the same thing as running the bracket, however, its just sending the data you see in the terminal into the backend API for the frontend to pull from

# TODO: Add "Run Bracket" and "Clear Bracket" button
# TODO: change final match in bracket to match the previous matches


app = Flask(__name__)

@app.route("/brackets")
def brackets():
    bracket = Bracket("Bracket Tracker Tournament")
    bracket.runBracket()
    
    data = {
        "bracket_name": bracket.bracketName,
        "teams": [team.getTeamName() for team in bracket.teams],
        "matchups_round1": [{
            "match_name": matchup.getMatchName(),
            "winner": matchup.getWinner().getTeamName(),
            "loser": matchup.getLoser().getTeamName()
        } for matchup in bracket.matchups_round1],
        "matchups_round2": [{
            "match_name": matchup.getMatchName(),
            "winner": matchup.getWinner().getTeamName(),
            "loser": matchup.getLoser().getTeamName()
        } for matchup in bracket.matchups_round2],
        "final_matchup": {
            "match_name": bracket.final_matchup.getMatchName(),
            "winner": bracket.final_matchup.getWinner().getTeamName(),
            "loser": bracket.final_matchup.getLoser().getTeamName()
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
