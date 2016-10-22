def break_words(stuff):
    words = stuff.split(' ')
    return words


def sort_words(words):
    return sorted(words)


def print_first_word(words):
    print words.pop(0)


def print_last_word(words):
    print words.pop(-1)


def sort_sentence(sentence):
    words = break_words(sentence)
    return sorted(words)


def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = break_words(sentence)
    words = sort_words(words)
    print_first_word(words)
    print_last_word(words)