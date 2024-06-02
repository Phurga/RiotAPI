from data_functions import read_pkl, MATCH_INFO_PATH, HIGHLIGHTS_PATH, write_pkl

all_matches_data = read_pkl(MATCH_INFO_PATH)

my_puuid = "X6eorlmrPyiYOP5tJ2eq7vBZistPMAnKA2-JKpBiRvlTSETpLb0bCxDso5H8vax78nCOzLElKaOvgg"

champions_highlights = dict()
max_stats = ['pentaKills','totalDamageDealtToChampions', 'kills', 'goldEarned']
max_challenges_stats = ['skillshotsDodged', 'damagePerMinute', 'teamDamagePercentage', 'deathsByEnemyChamps']
total_stats = ['pentaKills']
boolean_stats = ['win']
categorical_stats = ['role']

for k in range(len(all_matches_data)):
    match_data = next(iter(all_matches_data[k].values()))
    if match_data is None:
        continue
    for player_data in match_data['info']['participants']:
        if player_data['puuid'] != my_puuid:
            continue
        champion_name = player_data['championName']
        if champion_name not in champions_highlights:
            champions_highlights.update({champion_name: {key: player_data[key] for key in max_stats}})
            champions_highlights[champion_name].update({key: player_data['challenges'][key] for key in max_challenges_stats})
            for key in total_stats:
                champions_highlights[champion_name][f'total_{key}'] = player_data[key]
        else:
            for key in max_stats:
                if champions_highlights[champion_name][key] < player_data[key]: 
                    champions_highlights[champion_name][key] = player_data[key]
            for key in max_challenges_stats:
                if champions_highlights[champion_name][key] < player_data['challenges'][key]: 
                    champions_highlights[champion_name][key] = player_data['challenges'][key]
            for key in total_stats:
                champions_highlights[champion_name][f'total_{key}'] += player_data[key]

write_pkl(champions_highlights, HIGHLIGHTS_PATH)