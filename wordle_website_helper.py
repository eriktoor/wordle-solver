

import random 

from wordle_utils import all_letter_dictionaries, one_letter_dictionary, get_all_words, get_possible_words

def guess_word(words, guess, letters_not_in, letters_in_wrong_place, letters_in_right_place):

    letters_in_right_space = ['','','','','']
    letters_not_in_word = []
    letters_in_word_in_wrong_space = [[],[],[],[],[]]

    for idx in range(5): 
        letters_in_right_place = input("What letters are correct and in the word at space {idx} (if there are none press enter): ".format(idx=idx)).strip()
        letters_in_word_in_wrong_space_input = input("What letters are incorrect and not in the word at space {idx} (if there are none press enter): ".format(idx=idx)).strip()
        letters_not_in_word_anywhere = input("What letters are in the word but in the wrong space at space {idx} (if there are none press enter))".format(idx=idx)).strip()

        if letters_not_in_word_anywhere != "":
            letters_not_in_word.append(letters_not_in_word_anywhere)
        
        if letters_in_right_place != "":
            letters_in_right_space[idx] = letters_in_right_place
        
        if letters_in_word_in_wrong_space_input != "":
            letters_in_word_in_wrong_space.append(letters_in_word_in_wrong_space_input)


    return letters_not_in_word, letters_in_word_in_wrong_space, letters_in_right_space


def remove_letters_not_in_word(words, letters_not_in_word):

    end = len(words)-1
    curr = 0 
    increment = True 

    while curr < end: 
        word = words[curr]
        for t in letters_not_in_word: 
            if t in word: 
                words[curr], words[end] = words[end], words[curr] # move word to end  
                end -= 1 
                increment = False 
                break
        if increment: 
            curr += 1 
        increment = True        

    for t in letters_not_in_word: 
        if t in words[end]: 
            return words[:end]

    return words[:end+1]

def remove_words_with_letters_in_wrong_places(words, letters_in_wrong_place):

    end = len(words)-1
    curr = 0 
    increment = True 

    while curr <= end: 
        word = words[curr]
        for letter, place in letters_in_wrong_place: 
            if letter == word[place]: 
                words[curr], words[end] = words[end], words[curr] # move word to end  
                end -= 1 
                increment = False 
                break
        if increment: 
            curr += 1 
        increment = True        

    return words[:end+1]


def remove_words_with_letters_not_in_right_place(words, letters_in_right_place):

    end = len(words)-1
    curr = 0 
    increment = True 

    while curr <= end: 
        word = words[curr]
        for place, letter in enumerate(letters_in_right_place): 
            if letter == "":
                continue 
            if letter != word[place]: 
                words[curr], words[end] = words[end], words[curr] # move word to end  
                end -= 1 
                increment = False 
                break
        if increment: 
            curr += 1 
        increment = True        

    return words[:end+1]

def main(): 
    # STEP 1: READ THE FILE AND TURN IT INTO A WORDSLSIT 
    words = get_all_words()

    # STEP 2: Make dictionaries for each letter placement 
    l1, l2, l3, l4, l5 = all_letter_dictionaries(words)

    letters_in_right_place = ["", "", "", "", ""]

    # STEP 3: Make a guess, get feedback on letters not in and letters in wrong place 
    for guess in range(6):

        letters_not_in_word = []
        letters_in_wrong_place = []

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


        print("----------------------------------------------")




if __name__ == "__main__":
    main()
