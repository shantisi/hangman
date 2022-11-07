import string
from words import choose_word 
from images import IMAGES
def ifValid(user_input):
  if len(user_input) != 1:
    return False
  if not user_input.isalpha():
    return False
  return True  

def is_word_guessed(secret_word, letters_guessed):
  if secret_word==get_guessed_word(secret_word,letters_guessed):
    return True     
    
  return False

def get_guessed_word(secret_word, letters_guessed):
    
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word

def get_available_letters(letters_guessed):
    
    import string
    all_letters= string.ascii_lowercase
    letter_left=""
    for letter in all_letters:
      if letter not in letters_guessed:
        letter_left+=letter

    return letter_left

def get_hint(secret_word, letters_guessed):
  import random
  letters_not_guessed = []
  for i in secret_word:
    if i not in letters_guessed:
      if i not in letters_not_guessed:
        letters_not_guessed.append(i)

  return random.choice(letters_not_guessed)

def hangman(secret_word):
   
    print ("        ***Welcome to the game, Hangman!***         ")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " lettaers long.")
    print ("")
    # print(secret_word)   
    letters_guessed = []
    total_lives=remaining_lives=8
    image_selection=[0,1,2,3,4,5,6,7]
    level=input("enter the level in which you want to play""\n""a for easy""\n""b for medium""\n""c for hard level""\n")
    if level not in ["a","b","c"]:
      print("")
    if level=="b":
        total_lives=remaining_lives=6
        image_selection=[1,2,3,4,6,7]
    elif level=="c":
        total_lives=remaining_lives=4
        image_selection=[1,3,5,7]
    else:
        if level!="a":
          print("your choise is invalid""\n""game is starting in easy level")


    
    while remaining_lives>0:
      available_letters = get_available_letters(letters_guessed)
      print ("Available letters: " + available_letters)

      guess =input("Please guess a letter: ")
      letter = guess.lower()
      if letter=="hint":
        print("your hint for this secret word is",get_hint(secret_word,letters_guessed))

      else:
        if (not ifValid(letter))and letter!="hint":
          print("invalid input")
          continue


      if letter in secret_word:
          letters_guessed.append(letter)
          print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          print ("")

          if is_word_guessed(secret_word, letters_guessed) == True:
              print (" * * Congratulations, you won! * * ")
              print ("")
              break

      else:
          print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
          letters_guessed.append(letter)
          print(IMAGES[image_selection[total_lives-remaining_lives]])
          print("remaining_live: ",remaining_lives)
          remaining_lives-=1
          print ("")
    else:
      print("sorry you lose the game, the word was-",secret_word)      
    

secret_word = choose_word()
hangman(secret_word)
	
	
	
