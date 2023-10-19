import React from 'react';
import './style.css';

function ResultPage({ result }) {
  return (
    <div className="container">
      <h1>Résultat de la prédiction</h1>
      <p>Winner: {result}</p>
    </div>
  );
}

export default ResultPage;
