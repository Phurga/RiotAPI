from data_functions import write_pkl, read_pkl, write_json, MATCH_IDS_PATH, MATCH_DATA_PATH
from api_functions import get_match_data, api_call
import Profiles

def get_matches_data(profile: Profiles.Profile):
    game_data = []
    game_ids = read_pkl(f'{MATCH_IDS_PATH}{profile.suffix}')
    id_count = len(game_ids)
    for index, game_id in enumerate(game_ids):
        print(index/id_count, end='\r')
        try:
            game_data.append({game_id: get_match_data(game_id)})
        except ValueError: # Raised when there is no match_data available
            pass

    write_pkl(game_data, f'{MATCH_DATA_PATH}{profile.suffix}')
    #write_json(game_data, f'{MATCH_DATA_PATH}{profile.suffix}') loong
    return game_data

if __name__ == '__main__':
    get_matches_data(Profiles.ADRIEN)
    print(api_call.counter)