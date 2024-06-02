from data_functions import read_pkl, MATCH_DATA_PATH, HIGHLIGHTS_PATH, RESULT_PATH, write_pkl
import Profiles

import pandas as pd
import matplotlib.pyplot as plt
import time

def get_last_game_date(all_matches_data):
    def get_date(index):
        epochTime = next(iter(all_matches_data[index].values()))['info']['gameCreation']
        date = time.strftime("%Y-%m-%d", time.gmtime(epochTime / 1000))
        return date
    return get_date(-1), get_date(0)

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
        if match_data['info']['gameMode'] not in ['CLASSIC', 'ARAM'] or len(match_data['info']['participants']) != 10:
            continue
        for player_data in match_data['info']['participants']:
            if player_data['puuid'] != profile.puuid or player_data['gameEndedInEarlySurrender']:
                continue
            champion_name = player_data['championName']
            if champion_name in champions_highlights:
                for key in max_stats:
                    if champions_highlights[champion_name][key] < player_data[key]:
                        champions_highlights[champion_name][key] = player_data[key]
                for key in max_challenges_stats:
                    if champions_highlights[champion_name][key] < player_data['challenges'][key]: 
                        champions_highlights[champion_name][key] = player_data['challenges'][key]
                for key in total_stats:
                    champions_highlights[champion_name][f'total_{key}'] += player_data[key]
                for key in boolean_stats:
                    champions_highlights[champion_name][f'_{key}_gameCount'] += 1
                    champions_highlights[champion_name][f'_{key}_trueCount'] += player_data[key] * 1
                    champions_highlights[champion_name][f'{key}_rate'] = champions_highlights[champion_name][f'_{key}_trueCount'] / champions_highlights[champion_name][f'_{key}_gameCount']

            else: # else needs for initialisating
                champions_highlights.update({champion_name : {}})
                for key in max_stats:
                    champions_highlights[champion_name][key] = player_data[key]
                for key in max_challenges_stats:
                    champions_highlights[champion_name][key] = player_data['challenges'][key]
                for key in total_stats:
                    champions_highlights[champion_name][f'total_{key}'] = player_data[key]
                for key in boolean_stats:
                    champions_highlights[champion_name][f'_{key}_gameCount'] = 1
                    champions_highlights[champion_name][f'_{key}_trueCount'] = player_data[key] * 1
                    champions_highlights[champion_name][f'{key}_rate'] = champions_highlights[champion_name][f'_{key}_trueCount'] / champions_highlights[champion_name][f'_{key}_gameCount']

    write_pkl(champions_highlights, f"{HIGHLIGHTS_PATH}{profile.suffix}")

    # Showing info
    df = pd.DataFrame.from_dict(champions_highlights, orient='index')
    user = profile.suffix
    gameCount = len(df)
    date_past, date_recent = get_last_game_date(all_matches_data)
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
    df[df['total_pentaKills'] > 0]['total_pentaKills'].head(10).sort_values(ascending=False).plot(kind='bar', ax=axes[0,0], title="Total pentakills")
    df.nlargest(10,'teamDamagePercentage')['teamDamagePercentage'].sort_values(ascending=False).plot(kind='bar', ax=axes[0,1], title="Team Damage Percentage")
    df.nlargest(10,'skillshotsDodged')['skillshotsDodged'].sort_values(ascending=False).plot(kind='bar', ax=axes[1,0], title="Dodged skillshots")
    df['losses'] = df['_win_gameCount'] - df['_win_trueCount']
    df.nlargest(10,'_win_gameCount').sort_values(ascending=False, by='_win_gameCount')[['_win_trueCount', 'losses']].plot(kind='bar', ax=axes[1,1], title="Most played champions")
    fig.suptitle(f'Main results for {user}. {gameCount} games between {date_past} and {date_recent}.')
    plt.tight_layout()
    plt.savefig(f"{RESULT_PATH}{profile.suffix}") 
    plt.show()
    return champions_highlights

if __name__ == '__main__':
    get_champion_highlights(Profiles.LEO)