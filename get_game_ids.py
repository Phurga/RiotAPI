from api_functions import *
from data_functions import  *

import time

def find_last_valid_match(my_matches):
    match_info = None
    n = 1
    while match_info is None:
        try:
            my_last_match_id = my_matches[-n]
            match_info = get_match_data(my_last_match_id)
        except ValueError:
            n += 1
            print(n)
            pass
        # There can also be an Index error if there is no elements in my_matches. Handled in get_last_date.
    return match_info

def get_last_date(my_matches):
    match_info = find_last_valid_match(my_matches)
    gameEpochTime = match_info['info']['gameCreation']
    gameTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(gameEpochTime / 1000))
    print(f"{gameTime}")
    return gameEpochTime

def get_game_ids(gameName, tagLine):
    my_puuid = get_puuid(gameName, tagLine)
    game_id_list = []
    game_per_call = 100
    aram_queue_code = 450
    indexErrorCount = 0
    loopCount = 0
    while indexErrorCount < 10:
        loopCount += 1
        my_matches = get_last_matches(my_puuid, loopCount * game_per_call, game_per_call, aram_queue_code)
        try:
            get_last_date(my_matches)
            game_id_list.extend(my_matches)
        except IndexError:
            indexErrorCount += 1
            break
    write_pkl(game_id_list, f"{MATCH_IDS_PATH}_{gameName}_{tagLine}")

if __name__ == '__main__':
    get_game_ids("Aram%20Bagarre", "EUW")
    print(api_call.counter)