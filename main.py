from functions import *

import time

my_gameName = "Aram%20Bagarre"
my_tagLine = "EUW"

my_puuid = get_puuid(my_gameName, my_tagLine)
my_matches = get_last_matches(my_puuid)
my_last_match_id = my_matches[-1]
match_info = get_match_info(my_last_match_id)
gameEpochTime = match_info['info']['gameCreation']
gameTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(gameEpochTime / 1000))

print(gameTime)