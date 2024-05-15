import random


def print_hangman(num_of_tries):
    """
    prints the hangman according to the amount of mistakes
    :param num_of_tries: int that indicate how many tries has been made
    :return: none
    """
    HANGMAN_PHOTOS = {1: """        x-------x""", 2: """    x-------x
    |
    |
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
    print(HANGMAN_PHOTOS[num_of_tries])


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    checks if the input string is correct
    :param old_letters_guessed: all the letter guessed
    :type old_letters_guessed: list
    :param letter_guessed: string input from player
    :type letter_guessed: str
    :return if the letter guessed is one letter from the alphabet:
    """
    return not (len(letter_guessed) != 1 or not (letter_guessed.isalpha())
                or (letter_guessed in old_letters_guessed))


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    checks if the input is valid -
    the string contains only one letter from the alphabet that hasn't entered before
    :param letter_guessed:
    :param old_letters_guessed:
    :return:
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        return True

    print("X")
    sorted_list = sorted(old_letters_guessed)
    result = " -> ".join(str(x) for x in sorted_list)
    print(result)
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    represent the word need to be found according to what found or not
    :param secret_word: the word needed to be found
    :param old_letters_guessed: oll the pass letters
    :return: none
    """
    word_after_guess = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_after_guess.append(letter + " ")
        else:
            word_after_guess.append("_ ")
    print("".join(word_after_guess))


def check_win(secret_word, old_letters_guessed):
    """
    checks if all the word found
    :param secret_word: the word need to be found
    :param old_letters_guessed: what we guessed yet
    :return: if the letter found
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def check_if_guess_correct(secret_word, letter_guessed):
    """
    if the guess is correct
    :param secret_word: the word need to be found
    :param letter_guessed: what we guessed
    :return: non
    """
    return letter_guessed in secret_word


def choose_word(file_path, index):
    """
    return a random word from the file
    :param file_path: path to the words file
    :param index: the place of the word
    :return: the secret word
    """
    with open(file_path, 'r') as words_file:
        amount_of_single_show = 0
        words = words_file.read().split(' ')
        for word in words:
            if word.count(word) == 1:
                amount_of_single_show += 1

    while index > len(words):
        index -= len(words)
    return words[index]


HANGMAN_ASCII_ART = """Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ '
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
"""


def main():
    MAX_TRIES = 7
    num_of_tries = 0
    old_letters_guessed = []

    print(HANGMAN_ASCII_ART + "\n", MAX_TRIES, "\n")

    file_path = input("enter path to word file: ")
    location = int(input("enter word location"))
    secret_word = choose_word(file_path, location).lower()

    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        show_hidden_word(secret_word, old_letters_guessed)

        player_guess = input("Guess a letter: ").lower()

        if try_update_letter_guessed(player_guess, old_letters_guessed):
            old_letters_guessed.append(player_guess)

            if check_if_guess_correct(secret_word, player_guess):
                show_hidden_word(secret_word, old_letters_guessed)
            else:
                num_of_tries += 1
                print("):")
                print_hangman(num_of_tries)

    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOOS")


if __name__ == "__main__":
    main()
