import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

/*
  TODO:
  - draw connecting lines between matches
*/



// can get an API key if we want to get real time data of teams/games


const App = () => {
  return (
    <div className = "bracketTracker">
      <div className = "bracketHeaderTitle">
          <h1>Bracket Tracker Tournament</h1> 
      </div>
      
      <div className = "columns">
        <div className = "roundHeader">
          <h2>Round 1</h2>
        </div>

        <div className = "roundHeader">
          <h2>Round 2</h2>
        </div>

        <div className = "roundHeader">
          <h2>Final Round</h2>
        </div>
      </div>


      <div className = "columns">
        <div className = "round1MatchColumn">
        <div className = "match">
            <div className = "team">Team 1 
            <div className = "winOrLoss">W</div> 
            </div>
            <div className = "team">Team 2 
            <div className = "winOrLoss">L</div>
            </div>
          </div>

          <div className = "match">
            <div className = "team">Team 3
            <div className = 'winOrLoss'>W</div>
            </div>
            <div className = "team">Team 4
            <div className = 'winOrLoss'>L</div>
            </div>
          </div>

          <div className = "match">
            <div className = "team">Team 5
            <div className = 'winOrLoss'>W</div>
            </div>
            <div className = "team">Team 6
            <div className = 'winOrLoss'>L</div>
            </div>
          </div>

          <div className = "match">
            <div className = "team">Team 7
            <div className = 'winOrLoss'>W</div>
            </div>
            <div className = "team">Team 8
            <div className = 'winOrLoss'>L</div>
            </div>
          </div>
        </div>

        <div className = "round2MatchColumn">
        <div className = "match">
            <div className = "team">Team 1
            <div className = 'winOrLoss'>W</div>
            </div>
            <div className = "team">Team 3
            <div className = 'winOrLoss'>L</div>
            </div>
          </div>

          <div className = "match">
            <div className = "team">Team 5
            <div className = 'winOrLoss'>L</div>
            </div>
            <div className = "team">Team 7
            <div className = 'winOrLoss'>W</div>
            </div>
          </div>

        </div>

        <div className = "finalRoundMatchColumn">
        <div className = "match">
            <div className = "team">Team 1
            <div className = 'winOrLoss'>W</div>
            </div>
            <div className = "team">Team 7
            <div className = 'winOrLoss'>L</div>
            </div>
          </div>

        </div>
      </div>

    </div>
  );
};

export default App;
