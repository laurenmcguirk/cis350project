import React, { useState, useEffect } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
    // State variable to hold data from the backend
    const [data, setData] = useState(null)
    // detects if bracket is currently cleared or not
    // used to detect which interface was last interacted with (run button or clear button)
    const [bracketCleared, setBracketCleared] = useState(false);

    useEffect(() => {
        fetchData();
    }, []);
    // gets data from backend api
    const fetchData = () => {
        fetch("/bracket")
            .then(res => res.json())
            .then(data => {
                setData(data)
            });
    };

    // run bracket button interface
    const runBracket = () => {
        fetchData();
        setBracketCleared(false);
    }
    // clear bracket button interface
    const clearBracket = () => {
        setData(prevData => ({
            ...prevData,
            // clears team names and winner and loser symbols (W and L) from bracket
            matchups_round1: prevData.matchups_round1.map(matchup => ({ winner: '', loser: '' })),
            matchups_round2: prevData.matchups_round2.map(matchup => ({ winner: '', loser: '' })),
            final_matchup: { winner: '', loser: '' }
        }));
        setBracketCleared(true);
    };

    
    

    // Function to render each round's matchups
    const renderMatchups = (matchups) => {
        return (
            matchups.map((matchup, i) => (
                <div className="match" key={i}>
                    <div className="team">{matchup.winner}
                    <div className={`winOrLoss ${bracketCleared ? 'emptyWinOrLoss' : ''}`}>W</div>
                    </div>
                    <div className="team">{matchup.loser}
                        <div className={`winOrLoss ${bracketCleared ? 'emptyWinOrLoss' : ''}`}>L</div>
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
                                <div className={`winOrLoss ${bracketCleared ? 'emptyWinOrLoss' : ''}`}>W</div>

                                </div>
                                <div className="team">{data.final_matchup.loser}
                                <div className={`winOrLoss ${bracketCleared ? 'emptyWinOrLoss' : ''}`}>L</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </>
            )}
            <div className="bottomButton">
                <button className="buttonDesign" onClick={runBracket}>Run Bracket</button>
                <button className="buttonDesign" onClick={clearBracket}>Clear Bracket</button>
            </div>
        </div>
    );
}

export default App;
