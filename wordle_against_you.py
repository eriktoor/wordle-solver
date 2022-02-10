

import random 

from wordle_utils import all_letter_dictionaries, one_letter_dictionary, get_all_words, WORD_SIZE, get_possible_words

CORRECT_WORD = input("What word would you like this system to solve for? ").lower().strip()

def guess_word(words, guess, letters_not_in, letters_in_wrong_place, letters_in_right_place):

    for idx in range(len(guess)):
        if CORRECT_WORD[idx] == guess[idx]:
            letters_in_right_place[idx] = CORRECT_WORD[idx]
        elif guess[idx] in CORRECT_WORD: 
            letters_in_wrong_place[idx].append(guess[idx])
        else: 
            letters_not_in.append(guess[idx])

    return letters_not_in, letters_in_wrong_place, letters_in_right_place

def main(): 
    # STEP 1: READ THE FILE AND TURN IT INTO A WORDSLSIT 
    words = get_all_words()

    # STEP 2: Make dictionaries for each letter placement 
    l1, l2, l3, l4, l5 = all_letter_dictionaries(words)
    hmap = one_letter_dictionary(words)

    letters_in_right_place = ["", "", "", "", ""]

    # STEP 3: Make a guess, get feedback on letters not in and letters in wrong place 
    for guess in range(6):

        letters_not_in_word = []
        letters_in_wrong_place = [[],[],[],[],[]]

        word_to_guess = random.choice(words)

        if guess == 0: 
            word_to_guess = "crane"

        print("----------------------------------------------")
        print("Guess number: ", guess + 1)
        print("We are guessing: ", word_to_guess)

        letters_not_in_word, letters_in_wrong_place, letters_in_right_place  = guess_word(words, word_to_guess, letters_not_in_word, letters_in_wrong_place, letters_in_right_place)

        words = get_possible_words(words, letters_not_in_word, letters_in_wrong_place, letters_in_right_place)

        print("Letters not in the word: ", letters_not_in_word)
        print("Letters in the word but in the wrong place: ", letters_in_wrong_place)
        print("Letters in the right place: ", letters_in_right_place)
        print("We are down to ", len(words), " words")
        if len(words) < 30: 
            print(words)

        if CORRECT_WORD in words: 
            pass
        else:
            print("WE HAVE A BIG PROBLEM")


        print("----------------------------------------------")




if __name__ == "__main__":
    main()
