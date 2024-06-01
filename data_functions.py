import pickle

MATCH_FILE = 'data/data.pkl'

def store_match_ids(data):
    with open(MATCH_FILE, 'wb') as f:
        pickle.dump(data, f)

def read_match_ids():
    with open(MATCH_FILE, 'rb') as f:
        return pickle.load(f)
