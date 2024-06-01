from api_functions import *
from data_functions import  *

import time

def find_last_valid_match(my_matches):
    match_info = None
    n = 1
    while match_info is None:
        try:
            my_last_match_id = my_matches[-n]
            match_info = get_match_info(my_last_match_id)
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
    print(f"{gameTime} ({gameEpochTime})")
    return gameEpochTime

def get_game_ids(my_gameName, my_tagLine):
    
    my_puuid = get_puuid(my_gameName, my_tagLine)
    game_id_list = []
    count = 100
    aram_queue_code = 450
    for i in range(10):
        my_matches = get_last_matches(my_puuid, i * count, count, aram_queue_code)
        try:
            get_last_date(my_matches)
            game_id_list.extend(my_matches)
        except IndexError:
            break

    write_pkl(game_id_list, MATCH_IDS_PATH)

if __name__ == '__main__':
    my_gameName = "Aram%20Bagarre"
    my_tagLine = "EUW"
    #my_puuid = "X6eorlmrPyiYOP5tJ2eq7vBZistPMAnKA2-JKpBiRvlTSETpLb0bCxDso5H8vax78nCOzLElKaOvgg"
    get_game_ids(my_gameName, my_tagLine)
    print(api_call.counter)