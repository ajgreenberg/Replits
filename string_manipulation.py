import os, time

def colorChange(color):
  if color == "red":
    return("\033[31m")
  elif color == "white":
    return("\033[37m")
  elif color == "blue":
    return("\033[34m")
  elif color == "green":
    return("\033[32m")
  elif color == "pink":
    return("\033[35m")
  elif color == "yellow":
    return("\033[33m")

    
title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

print(f"    {title: ^35}")
print()
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"\t{colorChange('yellow')}Queen")
print()
print()
print(f"\t{colorChange('white')}PREV")
print(f"\t\t\t{colorChange('green')}NEXT")
print(f"\t\t\t\t\t{colorChange('pink')}PAUSE")

print()
print()
text = "WELCOME TO"
print(f"{colorChange('white')}{text:^35}")
text= "--  ARMBOOK  --"
print(f"{colorChange('blue')}{text:^35}")
print()
text = "definitely not a rip off of"
print(f"{colorChange('yellow')}{text:>35}")
text = "a certain other social"
print(f"{colorChange('yellow')}{text:>35}")
text="networking site"
print(f"{colorChange('yellow')}{text:>35}")
print()
text = "Honest."
print(f"{colorChange('red')}{text: ^35}")
print()
text  = "Username:"
username = input(f"{colorChange('white')}{text:^35}")
text  = "Password:"
username = input(f"{colorChange('white')}{text:^35}")
