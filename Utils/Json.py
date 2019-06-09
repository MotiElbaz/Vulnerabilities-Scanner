import json


def load_from_file(json_file):
    try:
        with open(json_file, encoding="utf8") as json_file:
            json_data = json.load(json_file)
            json_file.close()
    except ValueError as ve:
        print("Exception " + str(ve))
    return json_data


def save_file(json_str, json_file):
    try:
        with open(json_file, 'w') as f:
            json.dump(json_str, f)
            f.close()
    except ValueError as ve:
        print("Exception " + str(ve))
