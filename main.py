from api_functions import api_call
from get_game_ids import get_game_ids
from get_matches_data import get_matches_data

if __name__ == '__main__':
    my_gameName = "Nudibranchia"
    my_tagLine = "NUDI"
    get_game_ids(my_gameName, my_tagLine)
    get_matches_data(my_gameName, my_tagLine)
    print(api_call.counter)