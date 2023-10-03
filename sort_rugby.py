import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('rugby_dataset.csv')

# Convertir la colonne 'date' en format de date
df['date'] = pd.to_datetime(df['date'])

# Filtrer les lignes pour ne conserver que celles à partir de 2013
df = df[df['date'].dt.year >= 2013]

# Enregistrer le nouveau DataFrame dans un nouveau fichier CSV
df.to_csv('rugby_dataset_filtered.csv', index=False)
