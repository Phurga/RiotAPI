from data_functions import write_pkl, read_pkl, write_json, MATCH_IDS_PATH, MATCH_DATA_PATH
from api_functions import get_match_data, api_call

def get_matches_data(gameName, tagLine):
    file_id = f"{gameName}_{tagLine}"

    game_data = []
    for game_id in read_pkl(f'{MATCH_IDS_PATH}_{file_id}'):
        print(game_id)
        match_info = get_match_data(game_id)
        game_data.append({game_id: match_info})

    write_json(game_data, f'{MATCH_DATA_PATH}_{file_id}')
    write_pkl(game_data, f'{MATCH_DATA_PATH}_{file_id}')
    return game_data

if __name__ == '__main__':
    get_matches_data("Aram%20Bagarre", "EUW")
    print(api_call.counter)