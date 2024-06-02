from api_functions import *
from data_functions import  *
import Profiles

GAME_PER_CALL = 100

def get_game_ids(profile: Profiles.Profile) -> list[str]:
    """Gets all game ids for a given profile until the Riot base has no data."""
    game_ids = []
    loopCount = 0
    list_len = -1
    while list_len(game_ids) < len(game_ids): # If the game_ids list size does not increase anymore, no need to call the API anymore.
        if profile.queue_code is None:
            game_ids.extend(get_last_matches(profile.puuid, start = loopCount * GAME_PER_CALL, count = GAME_PER_CALL))
        else:    
            game_ids.extend(get_last_matches(profile.puuid, start = loopCount * GAME_PER_CALL, count = GAME_PER_CALL, queue = profile.queue_code))
        loopCount += 1
    write_pkl(game_ids, f"{MATCH_IDS_PATH}{profile.suffix}")
    return game_ids

if __name__ == '__main__':
    get_game_ids(Profiles.ADRIEN)
    print(api_call.counter)