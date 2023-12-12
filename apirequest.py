import pandas as pd
import requests

df = pd.read_csv('movies.csv')

for index, row in df.iterrows():
    # Film adını al
    film_name = row['name']

    api_key = 'e3509994'
    api_url = f"http://www.omdbapi.com/?apikey={api_key}&t={film_name}"

    response = requests.get(api_url)
    data = response.json()

    if 'Error' in data:
        print(f"Film adı: {film_name} - Hata: {data['Error']}")
    else:
        print(f"Film adı: {film_name} - Yıl: {data['Year']} - IMDb Puanı: {data['imdbRating']}")
