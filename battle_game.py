import os, time, random


def charGen():
  charName = input("Name Your Legend: ")
  print()
  return charName


def rollDice(side):
  result = random.randint(1, side)
  return result


def healthStats():
  health = (rollDice(6) * rollDice(12)) / 2 + 10
  return health


def strengthStats():
  strength = (rollDice(6) * rollDice(12)) / 2 + 12
  return strength


# generate Character 1
print("⚔️ Character Builder ⚔️")
print("**********************")
print()
time.sleep(1)
char1Name = charGen()
print(char1Name)
time.sleep(1)
char1Health = healthStats()
print("HEALTH:", char1Health)
time.sleep(1)
char1Strength = strengthStats()
print("STRENGTH:", char1Strength)
time.sleep(1)
print()
time.sleep(1)

# generate Character 2
print("Who are they battling?")
time.sleep(1)
print()
time.sleep(1)
char2Name = charGen()
print(char2Name)
time.sleep(1)
char2Health = healthStats()
print("HEALTH:", char1Health)
time.sleep(1)
char2Strength = strengthStats()
print("STRENGTH:", char2Strength)
time.sleep(1)
print()
time.sleep(1)

# start battle
os.system("clear")
print("⚔️ Battle Time ⚔️")
print("******************")
print()
time.sleep(1)
print("The battle begins!")
time.sleep(1)
print()
round = 0
while True:
  round += 1
  char1Roll = rollDice(6)
  char2Roll = rollDice(6)
  damage = abs(char1Strength - char2Strength) + 1
  if char1Roll > char2Roll:  # if char1 wins round
    char2Health -= damage
    time.sleep(1)
    print(char1Name, "wins round", round)
    time.sleep(1)
    print()
    print(char2Name, "takes a hit, with", damage, "damage")
     
  elif char2Roll > char1Roll:  # if char2 wins round
    char1Health -= damage
    time.sleep(1)
    print(char2Name, "wins round", round)
    time.sleep(1)
    print()
    print(char1Name, "takes a hit, with", damage, "damage")

  print()
  time.sleep(1)
  print(char1Name)
  time.sleep(1)
  print("HEALTH:", char1Health)
  print()
  time.sleep(1)
  print(char2Name)
  print("HEALTH:", char2Health)
  time.sleep(1)
  print()
  
  if char1Health < 0:
    print("Oh no", char1Name, "has died!")
    print()
    time.sleep(1)
    print(char2Name, "destroyed", char1Name, "in", round, "rounds!")
    break
  elif char2Health < 0:
    print("Oh no", char2Name, "has died!")
    print()
    time.sleep(1)
    print(char1Name, "destroyed", char2Name, "in", round, "rounds!")
    break
  else:
    os.system("clear")
    time.sleep(1)
    print("The battle continues!")
    print()
    time.sleep(1)
    print("Round", round + 1)
    time.sleep(1)
    print("*******")
    print()
