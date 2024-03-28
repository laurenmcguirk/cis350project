from flask import Flask, jsonify
from bracketClass import Bracket


# This runs the bracket and sends data to the backend API for the frontend to pull from

app = Flask(__name__)

@app.route("/bracket")
def brackets():
    bracket = Bracket("Bracket Tracker Tournament")
    bracket.runBracket()
    
    # data consists of title, team names, winners, and losers ordered in rounds
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
