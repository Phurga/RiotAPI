import pickle
import json

MATCH_IDS_PATH = 'data/match_ids'
MATCH_DATA_PATH = 'data/match_data'
HIGHLIGHTS_PATH = 'data/highlights'
RESULT_PATH = "output/results"

def write_pkl(data, path):
    """Path should not include the file extension"""
    with open(path+'.pkl', 'wb') as f:
        pickle.dump(data, f)
    return

def read_pkl(path):
    with open(path+'.pkl', 'rb') as f:
        return pickle.load(f)

def write_json(data, path):
    with open(path+'.json', 'w') as f:
        json.dump(data, f)
    return