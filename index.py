import pandas as pd
from datetime import datetime

# 1. Lire les fichiers
countries_df = pd.read_csv('countries.csv')
cities_df = pd.read_csv('cities.csv')
weather_df = pd.read_parquet('daily_weather.parquet')
result_df = pd.read_csv('rugby_dataset.csv')

result_df['date'] = pd.to_datetime(result_df['date'])

# Fusionner weather_df avec cities_df pour obtenir la correspondance pays
merged_df = pd.merge(weather_df, cities_df, on='station_id', how='left')

# 2. Filtrer countries_df pour ne conserver que les codes ISO des pays mentionnés en anglais
countries_to_keep = [
    "Argentina", "Australia", "England", "France", "Ireland",
    "Italy", "New Zealand", "Scotland", "South Africa", "Wales"
]
iso_codes_to_keep = countries_df[countries_df['country'].isin(
    countries_to_keep)]['iso3'].tolist()

# 3. Filtrer merged_df en fonction des codes ISO des pays
filtered_weather_df = merged_df[merged_df['iso3'].isin(iso_codes_to_keep)]

# 4. Filtrer pour ne conserver que les données des 10 dernières années
current_year = datetime.now().year
ten_years_ago = current_year - 10
filtered_weather_df = filtered_weather_df[filtered_weather_df['date'].dt.year > ten_years_ago]

# 5. Tri des résultats par date (du plus récent au plus ancien)
filtered_weather_df = filtered_weather_df.sort_values(by='date', ascending=False)

# 6. Enregistrer le résultat dans un fichier CSV
filtered_weather_df.to_csv('donnees_filtrees.csv', index=False)
