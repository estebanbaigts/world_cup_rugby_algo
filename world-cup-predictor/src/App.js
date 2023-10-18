import React, { useState } from 'react';
import './App.css';

function App() {
  const [homeTeam, setHomeTeam] = useState('');
  const [awayTeam, setAwayTeam] = useState('');
  const [city, setCity] = useState('');
  const [result, setResult] = useState('');

  const handlePredict = () => {
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
        setResult(data.result); // Mettez à jour ici pour utiliser data.result
      })
      .catch(error => console.error('Error:', error));
  };
  

  return (
    <div className="app-container">
      <header className="header">
        <h1>Rugby Match Prediction</h1>
      </header>
      <div className="content">
        <div className="teams-input">
          <input type="text" placeholder="Home Team" value={homeTeam} onChange={(e) => setHomeTeam(e.target.value)} />
          <input type="text" placeholder="Away Team" value={awayTeam} onChange={(e) => setAwayTeam(e.target.value)} />
          <input type="text" placeholder="City" value={city} onChange={(e) => setCity(e.target.value)} />
        </div>
        <button onClick={handlePredict}>Predict</button>
        {result && <p>{result}</p>}
      </div>
    </div>
  );
}

export default App;
