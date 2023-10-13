import requests

url = "https://offer.cdn.begmedia.com/api/pub/v3/competitions/34/outrights?application=2&countrycode=fr&forceCompetitionInfo=true&language=fr&sitecode=frfr"
response = requests.get(url)

if response.status_code == 200:

    data = response.json()
 
    cotes_vainqueur = data['grouped_markets'][0]['markets'][0]['selections']

    print("Cotes des équipes :")
    for i, equipe in enumerate(cotes_vainqueur, start=1):
        nom_equipe = equipe[0]['name']
        cote = equipe[0]['odds']
        print(f"{nom_equipe}: {cote}")
else:
    print("La requête a échoué. Statut :", response.status_code)