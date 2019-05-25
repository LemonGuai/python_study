def break_word(stuff):
    """this function will break up word for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words."""
    return sorted(words)

def print_first_word(words):
    """prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
