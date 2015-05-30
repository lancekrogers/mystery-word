import random
import re


def user_instruct():
    print('''
    This is a game called mystery word.

    The rules are the same as hangman.

    Guess a word one letter at a time.

    You are allowed 8 wrong guesses.

    If you guess a letter that is found
    in the word, that guess will not count against
    you.

    Have fun and enjoy Mystery Word!


    ''')


# pull_words() function takes a word from a file and passes a random word
def pull_words():
    with open("/usr/share/dict/words") as dictionary:
        dictionary = dictionary.read().split()
        random_word = random.choice(dictionary)
        return random_word


# takes in random word and outputs the number of letters in that word
def random_word_length(random_word):
    letters_in_word = len(random_word)
    print("\nYour word contains {} letters".format(letters_in_word))
    return letters_in_word


# put random_word into a list of single letter strings
# use indexes to display the guessed letters in the
# proper order and "_" for the letters that haven't been
# guessed yet

def game_function(random_word):
    letter_list = [x for x in random_word]
    guess = input("\nGuess a letter ")
    guess = guess.lower()
    wrong_guess = 8
    guess_list = []
    #while wrong_guess != 0 or x in guess_list != x in letter_list :
       # if guess in letter_list:
          #  guess_list = [guess_list].append(guess)
         #   print(guess)
        #    continue
     #   elif len(guess) > 1:
        #    print("Sorry guess must be a single letter. Try again.")
         #   break
       # elif guess == re.match('^[A-Za-z]*$', guess):
        #    print("Sorry guess must be a letter")
         #   break
       # else:
        #    print("_")
         #   break
    print(letter_list)
    print(random_word)




def main():
    user_instruct()
    random_word = pull_words()
    random_word_length(random_word)
    game_function(random_word)

main()
