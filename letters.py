import json
from tqdm import tqdm

with open("dictionary.json") as f:
    dictionary = json.load(f)

def validate_word(letters : list, word : str) -> int:
    """
    Returns 0 if "word" can't be spelled with input "letters", else, returns "word" size
    """
    letters = letters.copy()
    for letter in word:
        if letter in letters:
            letters.remove(letter)
        else:
            return 0
    return len(word)

def get_best_word(letters : str) -> list:
    letter_list = [letter.lower() for letter in letters]

    best_words = []
    biggest_word_size = 0

    for word in tqdm(dictionary, "Looking through the dictionary..."):
        this_word_size = validate_word(letter_list, word)
        if this_word_size > biggest_word_size:
            best_words.clear()
            biggest_word_size = this_word_size
        if this_word_size == biggest_word_size:
            best_words.append(word.upper())

    return best_words

def run_letters():
    letters = input("Write all the letters in the board (e.g. 'AFSICEBBA')\n>>> ")
    print("\nThe best words found were...")
    for i, word in enumerate(get_best_word(letters),1):
        print(i, word)

if __name__ == "__main__":
    run_letters()