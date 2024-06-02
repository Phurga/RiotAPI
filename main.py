from api_functions import explicit_api_usage
from get_game_ids import get_game_ids
from get_matches_data import get_matches_data
from match_statistics import get_champion_highlights
import Profiles

@explicit_api_usage
def main(profile: Profiles.Profile):
    get_game_ids(profile)
    get_matches_data(profile)
    get_champion_highlights(profile)

    
if __name__ == '__main__':
    main(Profiles.GASPAR)
    #main(Profiles.ADRIEN)
    #main(Profiles.LEO)