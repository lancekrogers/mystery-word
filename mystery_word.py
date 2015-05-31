import random


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
        random_word = random_word.lower()
        return random_word


# takes in random word and outputs the number of letters in that word
def random_word_length(random_word):
    letters_in_word = len(random_word)
    print("\n########## Your word contains {} letters ############".format(letters_in_word))
    return letters_in_word



# game functions
def game(random_word):
    random_word = random_word
    wrong_guesses = ''
    correct_guesses = ''
    done = False
    unders = "_" * len(random_word)
    unders = list(unders)
    random_list = list(random_word)
    lives_left = 8

    while done == False:
        print("\n" + ''.join(unders))
        guess = input("\nGuess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("\n" + ''.join(unders))
            print("\nPlease enter a single letter\n")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("\n" + ''.join(unders))
            print("\n####### Please enter a letter #######\n")
        elif unders == random_list:
            print("\n" + ''.join(unders))
            print("####### You win! #######")
            done = True
        elif guess in wrong_guesses or guess in correct_guesses:
            print("\n" + ''.join(unders))
            print("\nWrong Guesses: {}".format(' '.join(wrong_guesses.upper())) + "\nYou have {} wrong guesses left".format(lives_left))
            print("Correct Guesses: {}".format(' '.join(correct_guesses.upper())))
            print("\n######## You have already guessed {} please guess again ########".format(guess.upper()))

        elif guess not in random_word:
            if len(wrong_guesses) >= 8:
                print("\n" + ''.join(unders))
                print("######## You ran out of guesses, the word was {}.  Please play again! #######".format(random_word))
                done = True
            elif guess not in random_word:
                if guess not in wrong_guesses:
                    wrong_guesses = wrong_guesses + guess
                    lives_left = lives_left - 1
                print("\n" + ''.join(unders))
                print("\nWrong Guesses: {}".format(' '.join(wrong_guesses.upper())) + "\nYou have {} wrong guesses left".format(lives_left))
                print("Correct Guesses: {}".format(' '.join(correct_guesses.upper())))
                print("######### {} is not in the word #########".format(guess.upper()))
        elif guess in random_word:
            correct_guesses = correct_guesses + guess

            for x, y in enumerate(random_word):
                # x is the index in enumerate(random_word) and y is the value in random_word in this case y is a letter
                # if the variable guess == y then the value in underscore corresponding to the same index value as the
                # letter in random_word will be replaced with the value in guess
                if guess == y:
                    unders[x] = y.upper()
                    print("\n" + ''.join(unders))
                    if unders == random_list:
                        print(''.join(unders))
                        print("You win!")
                        done = True

            print("\nWrong Guesses: {}".format(' '.join(wrong_guesses.upper())) + "\nYou have {} wrong guesses left".format(lives_left))
            print("Correct Guesses: {}".format(' '.join(correct_guesses.upper())))
            print("\n ####### Good job! {} is a correct letter #########".format(guess.upper()))




def main():
    user_instruct()
    random_word = pull_words()
    random_word_length(random_word)
    game(random_word)
main()
