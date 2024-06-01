#from functions import get_puuid, get_last_matches, get_match_info
#from globals import API_KEY, API_SOURCE

import time
import requests

API_KEY = "RGAPI-bb2a5e0a-e86c-4ef5-ac02-15258ea56515"
API_SOURCE = "https://europe.api.riotgames.com"

def api_call(api_endpoint: str, arguments: str, api_key = API_KEY, api_source = API_SOURCE):
    if '?' in arguments:
        key_join = '&'
    else:
        key_join = '?'
    api_url = f"{api_source}{api_endpoint}{arguments}{key_join}api_key={api_key}"
    response = requests.get(api_url)
    api_call.counter += 1 # I want to ensure I respect the API limits
    if response.ok:
        return response.json()
    else:
        raise ValueError(response.status_code)
api_call.counter = 0 # Initiliasing

def get_puuid(gameName: str, tagLine: str):
    return api_call(api_endpoint = "/riot/account/v1/accounts/by-riot-id/",
                    arguments = '/'.join([gameName, tagLine]))['puuid']

def get_last_matches(puuid):
    arguments = f"{puuid}/ids?start=0&count=20"
    return api_call(api_endpoint = "/lol/match/v5/matches/by-puuid/",
                arguments = f"{puuid}/ids?start=0&count=20")

def get_match_info(match_id):
    return api_call(api_endpoint = "/lol/match/v5/matches/",
                    arguments = match_id)

my_gameName = "Aram%20Bagarre"
my_tagLine = "EUW"

my_puuid = get_puuid(my_gameName, my_tagLine)
my_matches = get_last_matches(my_puuid)
my_last_match_id = my_matches[-1]
match_info = get_match_info(my_last_match_id)
gameEpochTime = match_info['info']['gameCreation']
gameTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(gameEpochTime / 1000))

print(gameTime)