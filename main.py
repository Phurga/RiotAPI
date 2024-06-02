from api_functions import api_call
from get_game_ids import get_game_ids
from get_matches_data import get_matches_data
from match_statistics import get_champion_highlights
import Profiles

def main(profile):
    get_game_ids(profile)
    get_matches_data(profile)
    get_champion_highlights(profile)

    
if __name__ == '__main__':
    main(Profiles.GASPAR)
    print(api_call.counter)