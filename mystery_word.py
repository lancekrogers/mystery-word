import random



# pull_words() function takes a word from a dicionary and passes a random word
def pull_words():
    with open("/usr/share/dict/words") as dictionary:
        dictionary = dictionary.read().split()
        random_word = random.choice(dictionary)
        pass
        print(random_word)
pull_words()
