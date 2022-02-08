window.addEventListener('keydown', (e) => {
    console.log(e)
  })
  
  
  function typeAndEnter(word){
     
  
      for (let i = 0; i < 5; i++) {
          window.dispatchEvent(new KeyboardEvent('keydown', {
            'key': word[i]
          }));
      }
      window.dispatchEvent(new KeyboardEvent('keydown', {
          'key': 'Enter'
      }));
  
     
  }
  
  function getNumGuesses(){
  
      var numGuesses = 0;  
     
      var boardState = document.querySelectorAll("game-app")[0].boardState
      for (let i = 0; i < boardState.length; i++) {
          if (boardState[i].length != 0) {
              numGuesses += 1;
          }
      }
      return numGuesses;
  }
  
  function getCorrectAndIncorrectLetters(numGuesses){
  
      var not_in_word = [];
      var not_in_right_place = [[],[],[],[],[]];
      var in_right_place = ['', '', '', '', ''];
     
      // STEP 1: Keep track of letters in right and in word but in wrong places 
      var boardState = document.querySelectorAll("game-app")[0].boardState
      var evaluations = document.querySelectorAll("game-app")[0].evaluations
      for (let i = 0; i < numGuesses; i++) {
          let currEval = evaluations[i];
          for (let j =0; j < currEval.length; j++) {
              if (evaluations[i][j] == "correct") {
                  in_right_place[j] = boardState[i][j];
              } else if (evaluations[i][j] == "present") {
                  not_in_right_place[j].push(boardState[i][j])
              } 
          }
      }

      // STEP 2: Look at absent letters 
      for (let i = 0; i < numGuesses; i++) {
        let currEval = evaluations[i];
        for (let j =0; j < currEval.length; j++) {
            if (evaluations[i][j] == "absent") {
                var letter_not_in_not_in_right_place = true;  
                for (let k = 0; k < 5; k++) { // only push if it's not already in and not in and not in another place
                    if (not_in_right_place[k].includes(boardState[i][j])) {
                      letter_not_in_not_in_right_place = false; 
                    }
                }
                if (in_right_place.includes(boardState[i][j])) {
                    letter_not_in_not_in_right_place = false; 
                }
                if (letter_not_in_not_in_right_place && !not_in_word.includes(boardState[i][j])) {
                  not_in_word.push(boardState[i][j])
                }


            }
        }
    }
  
      return [not_in_word, not_in_right_place, in_right_place];
  }
  
  
  function createLetterMaps(allWords) {
      var l1 = {};
      var l2 = {};
      var l3 = {};
      var l4 = {};
      var l5 = {};
      var allDictionaries = [l1, l2, l3, l4, l5]
  
      for (let i = 0; i < allWords.length; i++) {
          var word = allWords[i]
          for (let j = 0; j < 5; j++) {
              var letter = allWords[i][j]
              if (!allDictionaries[j][letter]) {
                  allDictionaries[j][letter] = [word];
              } else {
                  allDictionaries[j][letter].push(word);            
              }
          }
      }
  
      return allDictionaries
  }
  
  
  
  
  
  function removeLettersNotInWord(words, letters_not_in_word){
  
      let end = words.length - 1; 
      let curr = 0; 
      let increment = true; 
  
      while (curr <= end) {
          var word = words[curr]; 
          for (let i = 0; i < letters_not_in_word.length; i++) {
              let t = letters_not_in_word[i];
              if (word == undefined) {
                let temp = words[end];
                words[end] = words[curr]; 
                words[curr] = temp; 
                end -= 1; 
                increment = false; 
                break;   
              }
              if (word.includes(t)) { // pairwise swap
                  let temp = words[end];
                  words[end] = words[curr]; 
                  words[curr] = temp; 
                  end -= 1; 
                  increment = false; 
                  break; 
              }
          }
          if (increment) {
              curr +=1 ; 
          }
          increment = true; 
      }
  
      return words.slice(0,end+1)
      
  }


  function removeWordsWithLettersInWrongPlaces(words, letters_in_wrong_place) {
    let end = words.length - 1; 
    let curr = 0; 
    let increment = true; 

    while (curr <= end) {
        var word = words[curr]; 
        for (let i = 0; i < letters_in_wrong_place.length; i++) {
            for (let j = 0; j < letters_in_wrong_place[i].length; j++){
              let t = letters_in_wrong_place[i][j];
                if (t == word[i]) { // remove this word if it is in this exact spot
                    let temp = words[end];
                    words[end] = words[curr]; 
                    words[curr] = temp; 
                    end -= 1; 
                    increment = false; 
                    break; 
                } else if (!word.includes(t)) { // remove word if it does not have this letter at all 
                    let temp = words[end];
                    words[end] = words[curr]; 
                    words[curr] = temp; 
                    end -= 1; 
                    increment = false; 
                    break; 
                }                  
            }

        }
        if (increment) {
            curr +=1 ; 
        }
        increment = true; 
    }

    return words.slice(0,end+1)
  
}

function removeWordsWithLettersNotInRightPlaces(words, letters_in_right_place) {
    let end = words.length - 1; 
    let curr = 0; 
    let increment = true; 

    while (curr <= end) {
        var word = words[curr]; 
        for (let i = 0; i < letters_in_right_place.length; i++) {
              let t = letters_in_right_place[i];
                if (t == "") {
                    continue;
                }
                if (word == undefined) {
                    let temp = words[end];
                    words[end] = words[curr]; 
                    words[curr] = temp; 
                    end -= 1; 
                    increment = false; 
                    break;   
                  }
                if (t != word[i]) { // pairwise swap
                    let temp = words[end];
                    words[end] = words[curr]; 
                    words[curr] = temp; 
                    end -= 1; 
                    increment = false; 
                    break; 
                }                 
            

        }
        if (increment) {
            curr +=1 ; 
        }
        increment = true; 
    }

    return words.slice(0,end+1)
  
}


const sleep = ms => new Promise(r => setTimeout(r, ms));


async function solveProblem(){
    var freshRun = true; 
    for (let guess = getNumGuesses(); guess <= 6; guess++) {

        // STEP 1: Guess a word
        var word_guess = words[Math.floor(Math.random() * words.length)]
        if (guess == 0 ) {
            word_guess = "crane"
        } 


        console.log("-------------------------------------------------------------")

        if (guess > 0 && freshRun) {
            console.log("*** Rerunning userscript despite game being in progress"); 
        } else {
            typeAndEnter(word_guess)
            await sleep(2000);
            console.log("Size of list before guess no. " + guess + ": " + words.length)
            console.log("Entering word '" + word_guess + "' for try no. ", + guess)
        }
        freshRun = false; 

       
        // STEP 2: Get feedback from guessing
        var feedback = getCorrectAndIncorrectLetters(getNumGuesses())
        var letters_not_in = feedback[0]
        var letters_in_wrong_place = feedback[1]
        var letters_in_right_place = feedback[2]

        console.log("Letters not in word: " + letters_not_in)
        console.log("Letters in wrong place: 0:" + letters_in_wrong_place[0] + " 1:" + letters_in_wrong_place[1] + " 2:" + letters_in_wrong_place[2] + " 3:" + letters_in_wrong_place[3] + " 4:" + letters_in_wrong_place[4] )
        console.log("Letters in right place: " + letters_in_right_place)

        // STEP 3: Remove words from words list that no longer fit standards
        words = removeLettersNotInWord(words, letters_not_in)
        words = removeWordsWithLettersInWrongPlaces(words, letters_in_wrong_place)
        words = removeWordsWithLettersNotInRightPlaces(words, letters_in_right_place)


        console.log("Size of list after guess no. " + guess + ": " + words.length)
        if (words.length < 50) {
            console.log(words)
        }

        console.log("-------------------------------------------------------------")


    }
   
}
