import React, { useState } from 'react';
import './style.css';

function App() {
  const [homeTeam, setHomeTeam] = useState('');
  const [awayTeam, setAwayTeam] = useState('');
  const [result, setResult] = useState(null);

  const flagsPath = './flags';

  const flagForTeam = (team) => {
    if (team === 'Argentina' || team === 'Australia' || team === 'England' || team === 'France' ||
        team === 'Ireland' || team === 'Italy' || team === 'New-Zealand' || team === 'Scotland' ||
        team === 'South-Africa' || team === 'Wales') {
      return `${flagsPath}/${team}.png`;
    }
  };

  const flagImageStyle = {
    maxWidth: '300px',
    margin: '130px',
    height: 'auto',
  };

  const teams = [
    'Argentina',
    'Australia',
    'England',
    'France',
    'Ireland',
    'Italy',
    'New-Zealand',
    'Scotland',
    'South-Africa',
    'Wales',
  ];

  const handleResultClick = () => {
    const resultMessage = `${homeTeam} vs. ${awayTeam}`;
    setResult(resultMessage);
  };

  return (
    <div className="app-container">
      <div className="component">
        <div className="input-flags-container">
          <div className="input-flags1">
            <img src={flagForTeam(homeTeam)} alt={homeTeam} style={flagImageStyle} />
          </div>
          <div className="input-flags2">
            <img src={flagForTeam(awayTeam)} alt={awayTeam} style={flagImageStyle} />
          </div>
        </div>
        <div className="input-container">
          <div className="input-dropdown">
            <select
              className="input"
              onChange={(e) => setHomeTeam(e.target.value)}
              value={homeTeam}
            >
              <option value="">Home Team</option>
              {teams.map((team) => (
                <option key={team} value={team}>
                  {team}
                </option>
              ))}
            </select>
            <select
              className="input"
              onChange={(e) => setAwayTeam(e.target.value)}
              value={awayTeam}
            >
              <option value="">Away Team</option>
              {teams.map((team) => (
                <option key={team} value={team}>
                  {team}
                </option>
              ))}
            </select>
          </div>
          <input type="text" className="input" placeholder="Cities" />
          <button className="result-button" onClick={handleResultClick}>
            Result
          </button>
          {result && (
            <div className="result">
              <p>Result:</p>
              <p>{result}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
