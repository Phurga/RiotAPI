import pickle
import json

MATCH_IDS_PATH = 'data/data.pkl'
MATCH_INFO_PATH = 'data/match_info.pkl'

def write_pkl(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)
    return

def read_pkl(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def write_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)
    return