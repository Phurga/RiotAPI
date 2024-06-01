from data_functions import write_pkl, read_pkl, write_json, MATCH_IDS_PATH, MATCH_INFO_PATH
from api_functions import get_match_info

game_data = []
for game_id in read_pkl(MATCH_IDS_PATH):
    print(game_id)
    match_info = get_match_info(game_id)
    game_data.append({game_id: match_info})

write_json(game_data, 'data/match_info.json')
write_pkl(game_data, MATCH_INFO_PATH)