import json
from tqdm import tqdm

MAX_LETTERS = 9
MIN_LETTERS = 4

with open("raw_dictionary.json") as f:
    data = json.load(f)

valid_words = {}

for word in tqdm(data):
    word_length = len(word)
    if MIN_LETTERS <= word_length <= MAX_LETTERS:
        valid_words[word] = word_length

with open("dictionary.json", "w") as fp:
    json.dump(valid_words, fp)
