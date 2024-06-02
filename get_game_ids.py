from api_functions import *
from data_functions import  *
import Profiles
from perf_tracker import track_perf

GAME_PER_CALL = 100

@explicit_api_usage
@track_perf
def get_game_ids(profile: Profiles.Profile) -> list[str]:
    """Gets all game ids for a given profile until the Riot base has no data."""
    game_ids = []
    loopCount = 0
    while True:
        if profile.queue_code is None:
            response = get_last_matches(profile.puuid, start = loopCount * GAME_PER_CALL, count = GAME_PER_CALL)
        else:    
            response = get_last_matches(profile.puuid, start = loopCount * GAME_PER_CALL, count = GAME_PER_CALL, queue = profile.queue_code)

        if response == []: # The API starts answering empty lists if no data is available.
            break
        game_ids.extend(response)
        loopCount += 1

    write_pkl(game_ids, f"{MATCH_IDS_PATH}{profile.suffix}")
    return game_ids

if __name__ == '__main__':
    get_game_ids(Profiles.ADRIEN)