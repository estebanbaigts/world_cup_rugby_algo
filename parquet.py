import pandas as pd
import pyarrow.parquet as pq

# Charger les données depuis le fichier .parquet
table = pq.read_table('daily_weather.parquet')

# Convertir la table en DataFrame
df = table.to_pandas()

# Capitales à inclure dans le filtre
capitales = {
    'Fidji': 'Suva',
    'France': 'Paris',
    'Nouvelle Zélande': 'Wellington',
    'Afrique du Sud': 'Cap',
    'Argentine': 'Buenos Aires',
    'Angleterre': 'Londres',
    'Pays de Galles': 'Cardiff',
    'Irlande': 'Dublin'
}

# Filtrer le DataFrame par les capitales spécifiées
df_filtered = df[df['city_name'].isin(capitales.values())]

# Filtrer le DataFrame pour inclure les données à partir de 2013
df_filtered = df_filtered[df_filtered['date'] >= '2013-01-01']

# Afficher les premières lignes du DataFrame filtré
print(df_filtered.head())
