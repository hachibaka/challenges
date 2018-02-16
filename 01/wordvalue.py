from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        data = [x.strip() for x in f.readlines()]

    return data

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    return sum(LETTER_SCORES.get(ch,0) for ch in word.upper())

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()

    maxword = None
    maxlength = 0
    for word in words:
        wordlength = calc_word_value(word)
        if maxlength < wordlength:
            maxlength = wordlength
            maxword = word
    return maxword


if __name__ == "__main__":
    pass # run unittests to validate
