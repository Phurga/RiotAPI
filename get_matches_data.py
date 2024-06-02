from data_functions import write_pkl, read_pkl, MATCH_IDS_PATH, MATCH_DATA_PATH
from api_functions import get_match_data, explicit_api_usage
import Profiles
from perf_tracker import track_perf

@explicit_api_usage
@track_perf
def get_matches_data(profile: Profiles.Profile):
    """Gets all data about matches from a given profile based on the previously generated list of game ids."""
    game_data = []
    game_ids = read_pkl(f'{MATCH_IDS_PATH}{profile.suffix}')
    id_count = len(game_ids)
    for index, game_id in enumerate(game_ids):
        print(f'{index / id_count * 100:9.0f}%'.format(), end='\r')
        try:
            game_data.append({game_id: get_match_data(game_id)})
        except ValueError: # Raised when there is no match_data available
            pass

    write_pkl(game_data, f'{MATCH_DATA_PATH}{profile.suffix}')
    return game_data

if __name__ == '__main__':
    get_matches_data(Profiles.ADRIEN)
    explicit_api_usage()