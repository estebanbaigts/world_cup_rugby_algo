import React, { useState, useEffect} from 'react';
import './style.css';

function App() {
  const [homeTeam, setHomeTeam] = useState('');
  const [awayTeam, setAwayTeam] = useState('');
  const [city, setCity] = useState('');
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [progress, setProgress] = useState(0);

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

  const handlePredict = () => {
    setIsLoading(true);
    setProgress(0); // Réinitialisez la progression

    fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        home_team: homeTeam,
        away_team: awayTeam,
        city: city,
      }),
    })
      .then(response => response.json())
      .then(data => {
        setResult(data.result);
        setIsLoading(false); // Désactivez le chargement une fois que le résultat est reçu
      })
      .catch(error => {
        console.error('Error:', error);
        setResult('Error: Could not retrieve data.');
        setIsLoading(false); // Désactivez le chargement en cas d'erreur
      });
  };

  useEffect(() => {
    if (isLoading) {
      const interval = setInterval(() => {
        if (progress < 100) {
          setProgress(progress + 5);
        }
      }, 10); // Ajustez la vitesse de remplissage si nécessaire
      return () => clearInterval(interval);
    }
  }, [isLoading, progress]);

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
            <input
              type="text"
              className="input"
              placeholder="City"
              value={city}
              onChange={(e) => setCity(e.target.value)}
            />
          </div>
          <button className="result-button" onClick={isLoading ? null : handlePredict} disabled={isLoading}>
            {isLoading ? `${progress}%` : 'Predict Winner'}
          </button>
          {result && !isLoading && (
            <div className="result">
              <p>Winner:</p>
              <p>{result}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
