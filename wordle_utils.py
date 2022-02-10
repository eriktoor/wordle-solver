WORD_SIZE = 5 

def all_letter_dictionaries(words):
    letter_1, letter_2, letter_3, letter_4, letter_5 = {}, {}, {}, {}, {}

    for word in words: 
        if WORD_SIZE != len(word): 
            print("This word is not length ", WORD_SIZE, ":", word)
            continue
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


def one_letter_dictionary(words):
    hmap = {}

    for word in words: 
        if WORD_SIZE != len(word): 
            print("This word is not length ", WORD_SIZE, ":", word)
            continue
        for l in word: 
            if l in hmap: 
                hmap[l].append(word)
            else: 
                hmap[l] = [word]
    return hmap 

def get_all_words(write_to_file=False): 
    with open('static/words.txt') as f:
        file = f.read()
        lines = file.split("\n")

    if write_to_file:
        f = open("static/words_as_array.txt", "w")
        f.write(str(lines))
        f.close()

    return lines


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

def get_possible_words(words, letters_not_in_word, letters_in_wrong_places, letters_in_right_places):
    ret = [] 

    for word in words: 

        if word == "":
            continue

        # STEP 1: Remove All Words CONTAINING LETTERS NOT IN THE WORD
        letter_not_in_word = True 
        for letter in letters_not_in_word: 
            if letter in word: 
                letter_not_in_word = False 

        # STEP 2: Remove All Words With Letters in Incorect Places 
        letter_not_in_wrong_place = True 
        for idx, letters in enumerate(letters_in_wrong_places): 
            for letter in letters:
                if word[idx] == letter: 
                    letter_not_in_wrong_place = False  
 
         # STEP 3: Only keep words with letters in the right place 
        letter_in_right_place = True 
        for idx, letter in enumerate(letters_in_right_places): 
            if letter == "":
                continue
            if word[idx] != letter: 
                letter_in_right_place = False  

        if letter_not_in_word and letter_not_in_wrong_place and letter_in_right_place: ret.append(word)


    return ret  




if __name__ == "__main__":
    print(len(get_all_words()))

    print(get_possible_words(["abc", "abcd", "abcde", "ac"], ["d","e"], [[], ["b"]], ['']))
