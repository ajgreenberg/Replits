from getpass import getpass as input
p1 = input("Player1, what is your move (R,P,S)?: ")
p2 = input("Player2, what is your move(R,P,S)?: ")
if p1 == p2:
  print("It's a draw! You both selected",p1,"!")
elif p1 == "R" and p2 == "S" :
  print("Player 1's",p1,"dominates Player 2's",p2)
elif  p1 == "S" and p2 == "P":
    print("Player 1's",p1,"dominates Player 2's",p2)
elif  p1 == "P" and p2 =="R":
    print("Player 1's",p1,"dominates Player 2's",p2)
else:
  print("Player 2's",p2,"dominates Player 1's",p1)
