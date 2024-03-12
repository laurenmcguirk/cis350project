import React, { useState, useEffect } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
    // State variable to hold data from the backend
    const [data, setData] = useState(null)

    useEffect(() => {
        fetch("/brackets").then(
            res =>res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])

    

    // Function to render each round's matchups
    const renderMatchups = (matchups) => {
        return (
            matchups.map((matchup, i) => (
                <div className="match" key={i}>
                    <div className="team">{matchup.winner}
                        <div className="winOrLoss">W</div>
                    </div>
                    <div className="team">{matchup.loser}
                        <div className="winOrLoss">L</div>
                    </div>
                </div>
            ))
        );
    };

    // Render bracket
    return (
        <div className="bracketTracker">
            {data && (
                <>
                    <div className="bracketHeaderTitle">
                        <h1>{data.bracket_name}</h1>
                    </div>

                    <div className="columns">
                        <div className="roundHeader">
                            <h2>Round 1</h2>
                        </div>

                        <div className="roundHeader">
                            <h2>Round 2</h2>
                        </div>

                        <div className="roundHeader">
                            <h2>Final Round</h2>
                        </div>
                    </div>

                    <div className="columns">
                        <div className="round1MatchColumn">
                            {renderMatchups(data.matchups_round1)}
                        </div>

                        <div className="round2MatchColumn">
                            {renderMatchups(data.matchups_round2)}
                        </div>

                        <div className="finalRoundMatchColumn">
                            <div className="match">
                                <div className="team">{data.final_matchup.winner}
                                    <div className="winOrLoss">W</div>
                                </div>
                                <div className="team">{data.final_matchup.loser}
                                    <div className="winOrLoss">L</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </>
            )}
        </div>
    );
}

export default App;
