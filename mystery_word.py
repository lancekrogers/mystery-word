import random



def user_instruct():
    print('''
    This is a game called mystery word.\n
    The rules are the same as hangman. \n
    Guess a word one letter at a time. \n
    You are allowed 8 wrong guesses.\n
    If you guess a letter contained in\n
    the word that will not count against\n
    you.\n
    Have fun and enjoy Mystery Word!
    ''')
    pass


# pull_words() function takes a word from a dicionary and passes a random word
def pull_words():
    with open("/usr/share/dict/words") as dictionary:
        dictionary = dictionary.read().split()
        random_word = random.choice(dictionary)
        return random_word

random_word = pull_words()


def random_word_length(random_word):
    letters_in_word = len(random_word)
    print("Your word contains {} letters".format(letters_in_word))
    pass
random_word_length(random_word)
