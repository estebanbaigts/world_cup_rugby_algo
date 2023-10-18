import React, { useState } from 'react';

function App() {
  const [homeTeam, setHomeTeam] = useState('');
  const [awayTeam, setAwayTeam] = useState('');

  const flagsPath = './flags';

  const flagForTeam = (team) => {
    if (team === 'Argentina' || team === 'Australia' || team === 'England' || team === 'France' ||
        team === 'Ireland' || team === 'Italy' || team === 'New-Zealand' || team === 'Scotland' ||
        team === 'South-Africa' || team === 'Wales') {
      return `${flagsPath}/${team}.png`;
    }
  };

  const flagImageStyle = {
    maxWidth: '400px',
    margin: '100px',
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

  return (
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
        <input type="text" className="input" placeholder="Cities" />
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
    </div>
  );
}

export default App;
