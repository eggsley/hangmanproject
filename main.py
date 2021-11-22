import random 

secret_words = ["seed" , "plant" , "science", "python", "mathematics", "winner", "engineer", "learn", "entrepreneur", "computer"] # the list of secret words.

print("Welcome to the Hangman Game, developed by: Wesley, Semir and Kevin!") 
print("Try to guess the word, you have 10 guesses.")

def get_word(): # the get_word function chooses a random word from the list of secret words.
  return random.choice(secret_words)

def check_word(letter, listofletters): # the check_word function stores the index of the user's letter if it is correct.
  check = []
  for i in range(len(listofletters)):
    if listofletters[i] == letter:
      check.append(i)
  return check

# check_word_result processing:
def update_guess(check_word_result, current_status, secret_word):
  for index in check_word_result:
    current_status = current_status[:index] + secret_word[index] + current_status[index+1:] # everything except the specific index of the chosen letter is concealed by dashes.
  return current_status

def guess_letter(): # the guess_letter function asks the user to type in a letter, and checks whether the user types in more/less than one letter (in which it will ask the user to try again).
  user_letter = input("Type in a letter: ")
  while len(user_letter) > 1 or len(user_letter) <= 0:
    print("You entered more or less than one letter. Try again.")
    user_letter = input("Type in a letter: ")
  return user_letter

def play_game(): # the play_game function calls all of the functions together.
  secret_word = get_word()

  current_status = "-" * len(secret_word)
  print(current_status)
  count = 0
  while "-" in current_status:
    if count < 10:
      user_guess = guess_letter()

      check_word_result = check_word(user_guess, list(secret_word))

      updated_guess = update_guess(check_word_result, current_status, secret_word)

      current_status = updated_guess

      print(current_status)
      count = count + 1
    else:
      print("You ran out of guesses! The word was", secret_word + ".")
      break

while True:
  playagain = input("Do you want to play? Yes or No? ") # asks if the user would like to play again.
  if playagain == "Yes" or playagain == "yes":
    play_game()
  elif playagain == "No" or playagain == "no":
    print("Okay, bye!") 
    break
  else: 
    break