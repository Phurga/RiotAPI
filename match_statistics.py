from data_functions import read_pkl, MATCH_DATA_PATH, HIGHLIGHTS_PATH, write_pkl
import Profiles


def get_champion_highlights(profile: Profiles.Profile):
    all_matches_data = read_pkl(f"{MATCH_DATA_PATH}{profile.suffix}")

    champions_highlights = dict()
    max_stats = ['pentaKills','totalDamageDealtToChampions', 'kills', 'goldEarned']
    max_challenges_stats = ['skillshotsDodged', 'damagePerMinute', 'teamDamagePercentage', 'deathsByEnemyChamps']
    total_stats = ['pentaKills']
    boolean_stats = ['win']

    for k in range(len(all_matches_data)):
        match_data = next(iter(all_matches_data[k].values()))
        if match_data is None:
            continue
        for player_data in match_data['info']['participants']:
            if player_data['puuid'] != profile.puuid:
                continue
            champion_name = player_data['championName']
            if champion_name in champions_highlights:
                for key in max_stats:
                    if champions_highlights[champion_name][key] < player_data[key]: 
                        champions_highlights[champion_name][key] = player_data[key]
                for key in max_challenges_stats:
                    if champions_highlights[champion_name][key] < player_data['challenges'][key]: 
                        champions_highlights[champion_name][key] = player_data['challenges'][key]
                for key in boolean_stats:
                    if player_data[key] is True:
                        champions_highlights[champion_name][f'_{key}_gameCount'] += 1
                        champions_highlights[champion_name][f'_{key}_trueCount'] += player_data[key] * 1
                        champions_highlights[champion_name][f'{key}_rate'] = champions_highlights[champion_name][f'_{key}_trueCount'] / champions_highlights[champion_name][f'_{key}_gameCount']

            else: # else needs for initialisating
                for key in total_stats:
                    champions_highlights[champion_name][f'total_{key}'] += player_data[key]
                champions_highlights.update({champion_name: {key: player_data[key] for key in max_stats}})
                champions_highlights[champion_name].update({key: player_data['challenges'][key] for key in max_challenges_stats})
                for key in total_stats:
                    champions_highlights[champion_name][f'total_{key}'] = player_data[key]
                for key in boolean_stats:
                    champions_highlights[champion_name][f'_{key}_gameCount'] = 1
                    champions_highlights[champion_name][f'_{key}_trueCount'] = player_data[key] * 1
                    champions_highlights[champion_name][f'{key}_rate'] = champions_highlights[champion_name][f'_{key}_trueCount'] / champions_highlights[champion_name][f'_{key}_gameCount']

    write_pkl(champions_highlights, f"{HIGHLIGHTS_PATH}{profile.suffix}")
    return champions_highlights

def showTeamDamage(highlights_data):
    # Show most team dmg
    stat = 'teamDamagePercentage'
    extract = {champion: highlights_data[champion][stat] for champion in highlights_data}
    print(stat +':')
    print({k: v for k, v in sorted(extract.items(), key=lambda item: item[1], reverse=True)})

def showPentas(highlights_data):
    # Show champs with pentas
    print('pentakills:')
    for champion, data in highlights_data.items():
        if data['total_pentaKills'] > 0:
            print(champion + ': ' + str(data['total_pentaKills']))

if __name__ == '__main__':
    get_champion_highlights(Profiles.ADRIEN)