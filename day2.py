"""
Dzisiaj proponujemy pokorzystać trochę z API i zaciągnąć trochę danych "na żywo" (proponowane przez nas rapidapi 
ma tą zaletę, że jest darmowe po założeniu konta oraz można od razu pobrać snippety kodu w danym języku - ale można 
korzystać oczywiście z dowolnego źródła i techniki, web scrapping też dozwolony!). Jeśli ktoś ma dużo czasu zawsze 
można też do tej bajki dołozyć wizualizację 🤩
#KARTKA #Z #KALENDARZA
Napisz program, który po uruchomieniu wyświetla w czytelnej formie aktualną datę, godzinę, dzień tygodnia 
i pogodę/temperaturę/ciśnienie w zadanym mieście 
(wykorzystaj np. https://rapidapi.com/commu.../api/open-weather-map/endpoints - pamiętaj o 
poprawnym przeliczeniu jednostek np. temperatura z kelwinów na stopnie) oraz losowy cytat (np. https://type.fit/api/quotes ). 
Wykorzystaj requests i datetime.
Propozycja rozszerzenia: Wyświetl również bieżący czas dla miast w różnych strefach czasowych (np. Pekin, Sydney, Waszyngton, Londyn) - 
wykorzystaj np. pytz: https://pypi.org/project/pytz/ oraz wyświetl listę osób obchodzących imieniny (poszukaj otwartej 
bazy danych lub wykorzystaj prosty web scrapping np. z wykorzystaniem: https://imienniczek.pl/widget/js ).
"""
import requests
from datetime import datetime

def get_data(city):

    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":f"{city}","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

    headers = {
        'x-rapidapi-key': "MY_API_KEY",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def get_temp(city):
    response = get_data(city)
    return response['main']['temp']


def get_pressure(city):
    response = get_data(city)
    return response['main']['pressure']


def get_random_quote():
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        'x-rapidapi-key': "MY_API_KEY",
        'x-rapidapi-host': "quotes15.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    return response.json()


city = "London"
temp = round(get_temp(city) - 273, 2)
pressure = get_pressure(city)

today = datetime.today()
today_date = today.strftime("%A - %d/%m/%y %H:%M")

text_to_print = f'Today we have: {today_date}. Pressure {pressure}, Temperature {temp} degrees'
print(text_to_print)

quote = get_random_quote()
print(quote["content"])