import re

def edit_word(word):
    word = re.sub(r'\([^()]*\)', '', word)
    return word