

import random 

WORD_SIZE = 5 
CORRECT_WORD = input("What word would you like this system to solve for? ").lower().strip()

def guess_word(words, guess, letters_not_in, letters_in_wrong_place, letters_in_right_place):

    for idx in range(len(guess)):
        if CORRECT_WORD[idx] == guess[idx]:
            letters_in_right_place[idx] = CORRECT_WORD[idx]
        elif guess[idx] in CORRECT_WORD: 
            letters_in_wrong_place.append((guess[idx], idx))
        else: 
            letters_not_in.append(guess[idx])

    return letters_not_in, letters_in_wrong_place, letters_in_right_place


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

def get_all_words(): 
    with open('wordlist.txt') as f:
        file = f.read()
        lines = file.split("\n")

    f = open("demofile3.txt", "w")
    f.write(str(lines))
    f.close()
    return lines 

def all_letter_dictionaries(words):
    letter_1, letter_2, letter_3, letter_4, letter_5 = {}, {}, {}, {}, {}

    for word in words: 
        if WORD_SIZE != len(word): raise("THIS IS A PROBLEM")

        if word[0] not in letter_1:
            letter_1[word[0]] = [word]
        else: 
            letter_1[word[0]].append(word)

        if word[1] not in letter_2:
            letter_2[word[1]] = [word]
        else: 
            letter_2[word[1]].append(word)
        
        if word[2] not in letter_3:
            letter_3[word[2]] = [word]
        else: 
            letter_3[word[2]].append(word)

        if word[3] not in letter_4:
            letter_4[word[3]] = [word]
        else: 
            letter_4[word[3]].append(word)

        if word[4] not in letter_5:
            letter_5[word[4]] = [word]
        else: 
            letter_5[word[4]].append(word)

        return letter_1, letter_2, letter_3, letter_4, letter_5

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

        words = remove_letters_not_in_word(words, letters_not_in_word)
        words = remove_words_with_letters_in_wrong_places(words, letters_in_wrong_place)
        words = remove_words_with_letters_not_in_right_place(words, letters_in_right_place)
        

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
