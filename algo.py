import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
import requests
from googletrans import Translator

# Charger le fichier CSV
df = pd.read_csv('rugby_dataset_filtered.csv')

# Créer une nouvelle colonne 'winner' basée sur les points
df['winner'] = df.apply(lambda row: row['home_team'] if row['home_score'] > row['away_score'] else row['away_team'], axis=1)

# Diviser les données en ensembles d'entraînement et de test
X = df[['home_team', 'away_team', 'city']]
y = df['winner']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Utiliser OneHotEncoder pour les colonnes catégorielles
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

# Adapter et transformer l'ensemble d'entraînement
X_train_encoded = encoder.fit_transform(X_train[['home_team', 'away_team', 'city']])
X_train_encoded_df = pd.DataFrame(X_train_encoded, columns=encoder.get_feature_names_out(['home_team', 'away_team', 'city']))

# Transformer l'ensemble de test
X_test_encoded = encoder.transform(X_test[['home_team', 'away_team', 'city']])
X_test_encoded_df = pd.DataFrame(X_test_encoded, columns=encoder.get_feature_names_out(['home_team', 'away_team', 'city']))

# Entraîner un modèle de régression logistique pour la classification
model = LogisticRegression(max_iter=1000)
model.fit(X_train_encoded_df, y_train)

# Traducteur pour les noms d'équipes
team_translator = {
    'Angleterre': 'England',
    'France': 'France',
    'Irlande': 'Ireland',
    'Italie': 'Italy',
    'Écosse': 'Scotland',
    'Pays de Galles': 'Wales',
    'Afrique du Sud': 'South Africa',
    'Nouvelle-Zélande': 'New Zealand',
    'Australie': 'Australia',
    'Argentine': 'Argentina'
}

# Prédire le résultat d'un match en utilisant les cotes
def predict_result(home_team, away_team, city):
    # Récupérer les cotes des équipes
    odds_url = "https://offer.cdn.begmedia.com/api/pub/v3/competitions/34/outrights?application=2&countrycode=fr&forceCompetitionInfo=true&language=fr&sitecode=frfr"
    odds_response = requests.get(odds_url)

    if odds_response.status_code == 200:
        odds_data = odds_response.json()
        odds_dict = {}
        for selection in odds_data['grouped_markets'][0]['markets'][0]['selections']:
            team_name_fr = selection[0]['name']
            team_name_en = team_translator.get(team_name_fr)
            if team_name_en:
                odds_dict[team_name_en] = selection[0]['odds']
    else:
        print("La requête des cotes a échoué. Statut :", odds_response.status_code)
        odds_dict = {}

    # Transformer les entrées
    input_data = encoder.transform([[home_team, away_team, city]])
    input_df = pd.DataFrame(input_data, columns=encoder.get_feature_names_out(['home_team', 'away_team', 'city']))

    # Faire la prédiction
    prediction = model.predict(input_df)

    # Décoder la prédiction
    winner = prediction[0]

    # Calculer le pourcentage de victoire basé sur les deux dernières années
    win_percentage = df[(df['home_team'] == home_team) & (df['away_team'] == away_team)]['winner'].value_counts(normalize=True).get(winner, 0) * 100

    # Calculer les points possibles (arrondis à l'entier le plus proche)
    home_score = round(df[(df['home_team'] == home_team) & (df['away_team'] == away_team)]['home_score'].fillna(0).mean())
    away_score = round(df[(df['home_team'] == home_team) & (df['away_team'] == away_team)]['away_score'].fillna(0).mean())

    # Inverser les résultats si l'équipe à l'extérieur est prédite comme gagnante
    if winner == away_team:
        winner = home_team
        win_percentage = 100 - win_percentage
        home_score, away_score = away_score, home_score

    # Ajuster le pourcentage de victoire en fonction des cotes
    if winner in odds_dict:
        adjusted_win_percentage = win_percentage * (1 / odds_dict[winner]) * 1.5
    else:
        adjusted_win_percentage = win_percentage

    return f"Prédiction de résultat : {winner} gagne avec une probabilité ajustée de {adjusted_win_percentage:.2f}%. Scores possibles : {away_score}-{home_score}."

# Exemple d'utilisation
home_team = input("Nom de l'équipe à domicile : ")
away_team = input("Nom de l'équipe à l'extérieur : ")
city = input("Ville : ")

result_prediction = predict_result(home_team, away_team, city)
print(result_prediction)