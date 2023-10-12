print("TO DO LIST MANAGER:")
print("*******************")
print()
toDoList = []

def printList():
  print() 
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("Do you want to view, add, or edit your to do list: \n")
  print()
  if menu == "view":
    printList()
  elif menu =="add":
    item = input("What would you like to add to your To Do List?: \n")
    toDoList.append(item)
  elif menu == "remove":
    item = input("What have you completed?: \n")
    if item in toDoList:
      toDoList.remove(item)
    else:
      print(f"{item} was not in the list")
