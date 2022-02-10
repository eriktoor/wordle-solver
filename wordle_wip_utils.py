# MORE EFFICIENT WAY TO GET CORRECT WORDS

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
        for place, letters  in enumerate(letters_in_wrong_place): 
            for letter in letters:
                if letter == "":
                    continue 
                if len(word) != WORD_SIZE or letter == word[place]: 
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
            if len(word) != WORD_SIZE or letter == word[place]:                 
                words[curr], words[end] = words[end], words[curr] # move word to end  
                end -= 1 
                increment = False 
                break
        if increment: 
            curr += 1 
        increment = True        

    return words[:end+1]
