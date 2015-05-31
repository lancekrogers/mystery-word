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
    print("\nYour word contains {} letters".format(letters_in_word))
    return letters_in_word



# collect guesses
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
        print(random_word)
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print(str(unders))
            print("Please enter only a single letter")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print(''.join(unders))
            print("Please enter a letter")
        elif unders == random_list:
            print(''.join(unders))
            print("You win!")
            done = True
        elif guess in wrong_guesses or guess in correct_guesses:
            print(''.join(unders))
            print("You have already guessed {} please guess again".format(guess))
            print("\nWrong Guesses: {}".format(wrong_guesses) + "\nYou have {} wrong guesses left".format(lives_left))
            print("\nCorrect Guesses: {}".format(correct_guesses))

        elif guess not in random_word:
            if len(wrong_guesses) >= 8:
                print(''.join(unders))
                print("You ran out of guesses, the word was {}.  Please play again!".format(random_word))
                done = True
            elif guess not in random_word:
                wrong_guesses = wrong_guesses + guess
                lives_left = lives_left - len(wrong_guesses)
                print(''.join(unders))
                print("\nWrong Guesses: {}".format(wrong_guesses) + "\nYou have {} wrong guesses left".format(lives_left))
                print("\nCorrect Guesses: {}\n".format(correct_guesses))
                print("{} is not in the word".format(guess))
        elif guess in random_word:
            correct_guesses = correct_guesses + guess
            for x, y in enumerate(random_word):
                if guess == y:
                    unders[x] = y
                    print(''.join(unders))


            print("\nWrong Guesses: {}".format(wrong_guesses) + "\nYou have {} wrong guesses left".format(lives_left))
            print("\nCorrect Guesses: {}\n".format(correct_guesses))
            print("Good job! {} is a correct guess".format(guess.upper()))










def holds_guesses(random_word, guess):
    wrong_guesses = ''
    correct_guesses = ''
    random_word = random_word
    guess = guess
    if guess in random_word:
        correct_guesses = correct_guesses + 1
    elif guess not in random_word:
        wrong_guesses = wrong_guesses + guess




# put random_word into a list of single letter strings
# use indexes to display the guessed letters in the
# proper order and "_" for the letters that haven't been
# guessed yet

def mystery_variables(random_word):
    unders = "_" * len(random_word)
    random_word = random_word.lower()
    correct_guesses = [x for x in random_word]


    while wrong_guesses >= 0 or guess_list != correct_guesses:
        guess = input("Guess a letter ")
        guess = guess.lower()
        if guess not in correct_guesses:
            wrong_guesses -= 1
            print("You have {} more wrong guesses left.".format(wrong_guesses))
            if wrong_guesses <= 0:
                print("You lose! Wish I had put some money on this game")
                break
        elif guess in correct_guesses:
            for guess in correct_guesses:
                unders = [guess for index in unders]

                print(guess_list)
                print(random_word)

            print("Correct!")




def main():
    user_instruct()
    random_word = pull_words()
    random_word_length(random_word)
    game(random_word)
main()
