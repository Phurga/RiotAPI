# Purpose
The main program (main.py) generates a summary of a lol player performances over available game data retrieved from the RIOT API (https://developer.riotgames.com/).

# How to
1. Get a valid python environment by loading the provided environment.yml file (if using conda: $conda env create -f environment.yml)
1. Get your RIOT API KEY (valid 24h) and update the API_KEY variable in api_functions.py. Otherwise you will get error 403.
1. Run the main.py program.
1. If you want to change the users to generate data about, you need to change the profiles called by main(profile) in the main.py program. You may need to add new profiles in the Profiles.py file.
1. This will generate png files in the "output" folder. But also some data in the "data" folder under the pickle format. You can load these in notebooks and play with the data.
1. Be mindful that the RIOT API has call rates limitations, hence any API call in this program is done through a specific function having some overheads. 