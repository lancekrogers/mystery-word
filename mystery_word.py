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
    Have fun and enjoy Mystery Word!\n
    Press RETURN to continue.\n''')


# pull_words() function takes a word from a file and passes a random word
def pull_words():
    with open("/usr/share/dict/words") as dictionary:
        dictionary = dictionary.read().split()
        random_word = random.choice(dictionary)
        return random_word


# takes in random word and outputs the number of letters in that word
def random_word_length(random_word):
    letters_in_word = len(random_word)
    print("Your word contains {} letters".format(letters_in_word))
    return letters_in_word


# put random_word into a list of single letter strings
# use indexes to display the guessed letters in the
# proper order and "_" for the letters that havent been
# guessed yet
def game_function(random_word):
    letter_list = [x for x in random_word]
    print(letter_list)


user_instruct()
random_word = pull_words()
random_word_length(random_word)
game_function(random_word)
