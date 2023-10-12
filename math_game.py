print("Math Game!")
print("**********")
print()
base = int(input("Name your multiple:"))
score = 0
for i in range(1,11):
  answer = i * base
  print(i,"x",base,"=")
  guess = int(input())
  if guess == answer:
    print("Great work!")
    score += 1
  else: print("Nope, the answer was",answer)
print("You scored",score,"out of 10!")
    
