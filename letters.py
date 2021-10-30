import json

with open("dictionary.json") as f:
    dictionary = json.load(f)

def run_letters():
    print("run letters")