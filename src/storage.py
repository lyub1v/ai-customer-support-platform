import json

FILE_NAME = 'faqs_json'

def save_faqs(faqs):
    with open(FILE_NAME, 'w') as file:
        json.dump(faqs, file, indent=4)

def load_faqs():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('File is corrupted. Starting with empty FAQ list.')
        return []