import requests
from rate_limiter import rate_limiter, CALLS_LONG, CALLS_SHORT, PERIOD_LONG, PERIOD_SHORT


API_KEY = "RGAPI-768e624c-3fd5-4141-89cf-0ee1ea04b04c"
API_DICT = {"api_key" : API_KEY}
API_SOURCE = "https://europe.api.riotgames.com"


@rate_limiter(CALLS_LONG, PERIOD_LONG)
@rate_limiter(CALLS_SHORT, PERIOD_SHORT)
def api_call(api_endpoint: str, params = API_DICT, api_source = API_SOURCE):
    """ Some overhead over requests.get"""
    response = requests.get(f"{api_source}{api_endpoint}", params=params)
    api_call.counter += 1
    if response.ok:
        return response.json()
    else:
        raise ValueError(response.status_code)
api_call.counter = 0 # Initiliasing

def get_puuid(gameName: str, tagLine: str):
    return api_call(f"/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}")['puuid']

def get_last_matches(puuid, start, count, queue):
    params = {"start": start, "count": count, "queue": queue}
    params.update(API_DICT)
    return api_call(api_endpoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids", params=params)

def get_match_data(match_id):
    try:
        return api_call(api_endpoint = f"/lol/match/v5/matches/{match_id}")
    except ValueError:
        print(f"{match_id} has no data entry.")
        return None