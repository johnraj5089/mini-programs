import random 
def play(att,n):
  while att > 0:
    print (f"You have {att} attempts remaining to guess the number.")
    guess = int(input("Make a guess: ")) 
    att = check_guess(guess,n,att)
  if att == 0:
    print ("You have run out of guesses, you lose.")

def check_guess(guess,n,att):
  if guess == n:
      print (f"You got it. The answer was {n}")
      return -1
  elif guess > n:
      print ("Too high. \nGuess again.")
      return att-1
  else:
      print("Too low. \nGuess again.")
      return att-1

def level():
  diff = input ("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
  if diff == 'easy':
    return 10
  elif diff == 'hard':
    return 5

if __name__ == '__main__':
  print ("Welcome to the Number Guessing Game!")
  print ("I'm thinking of a number between 1 and 100.")
  num = random.randint(1,100)
  attempt = level()
  play(attempt,num)
