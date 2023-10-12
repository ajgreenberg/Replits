from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go to the home menu: "))
    if stop_playback == 2:
      source.paused = True
      return
    else:
      continue
    

while True:
  os.system("clear") # clear the screen 
  print("MyPod Music Player")
  print()
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anyting else to see the menu again")
  choice = int(input())
  if choice == 1:
    print("Playing some proper tunes!")
    play()
  elif choice == 2:
    exit()
  else: 
    continue
