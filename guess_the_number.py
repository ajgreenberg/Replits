print("One-Million-To-One Game")
print("************************")
print()
print("Guess a number between one and a million!")
print()
number = 50000
numberGuesses = 1
while True:
  guess = int(input("What is your guess?:"))
  if guess == number:
    print("Correct!")
    break
  elif guess < number and guess >=0 :
    print ("Too Low")
    numberGuesses += 1
    continue
  elif guess > number:
    print("Too high")
    numberGuesses += 1
    continue
  elif guess < 0:
    exit()
print("It took you", numberGuesses,"to get it correct!")
