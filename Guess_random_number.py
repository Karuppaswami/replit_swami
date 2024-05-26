import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def guess_number():
  number = random.randint(1,100)
  level_selection = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level_selection == "easy":
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")
  elif level_selection == "hard":
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")
  
  while attempts != 0:
    guess_number = int(input("Make a guess: "))
    if guess_number == number:
      print(f"You got it! The answer was {number}")
      break 
    elif guess_number > number:
      print("Too high.")
    elif guess_number < number:
      print("Too low.") 
      
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
    
  if attempts == 0:
    print("You lose the game.")
print(guess_number())