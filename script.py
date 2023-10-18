import pandas as pd
from datetime import datetime
import pyarrow.parquet as pq

countries_df = pd.read_csv('countries.csv')
cities_df = pd.read_csv('cities.csv')
weather_df = pd.read_parquet('daily_weather.parquet')
result_df = pd.read_csv('rugby_dataset.csv')
df = pd.read_csv('rugby_dataset.csv')

df['date'] = pd.to_datetime(df['date'])
df = df[df['date'].dt.year >= 2013]

result_df['date'] = pd.to_datetime(result_df['date'])

merged_df = pd.merge(weather_df, cities_df, on='station_id', how='left')

countries_to_keep = [
    "Argentina", "Australia", "England", "France", "Ireland",
    "Italy", "New Zealand", "Scotland", "South Africa", "Wales"
]
iso_codes_to_keep = countries_df[countries_df['country'].isin(
    countries_to_keep)]['iso3'].tolist()

filtered_weather_df = merged_df[merged_df['iso3'].isin(iso_codes_to_keep)]

current_year = datetime.now().year
ten_years_ago = current_year - 10
filtered_weather_df = filtered_weather_df[filtered_weather_df['date'].dt.year > ten_years_ago]

filtered_weather_df = filtered_weather_df.sort_values(by='date', ascending=False)

filtered_weather_df.to_csv('donnees_filtrees.csv', index=False)
df.to_csv('rugby_filtered.csv', index=False)
