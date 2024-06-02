from api_functions import api_call
from get_game_ids import get_game_ids
from get_matches_data import get_matches_data
import Profiles

def main(profile):
    get_game_ids(profile)
    get_matches_data(profile)

    
if __name__ == '__main__':
    main(Profiles.ADRIEN)
    print(api_call.counter)