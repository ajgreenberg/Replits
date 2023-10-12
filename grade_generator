print("Exam Grade Calculator")
testName = input("What is the name of the test?: ")
possiblePoints = int (input ("What are the total possible points?: "))
yourScore = int (input ("What was your score?: "))
numberGrade = round(float((yourScore / possiblePoints)*100),2)
print(numberGrade,"%",sep='')
if numberGrade >=90:
  letterGrade = "A+"
elif numberGrade >=80 and yourScore <90:
  letterGrade = "A-"
elif numberGrade >=70 and yourScore <80:
  letterGrade = "B-"
elif numberGrade >=60 and yourScore <70:
  letterGrade = "C"
elif numberGrade >=50 and yourScore <60:
  letterGrade = "D"
else:
  letterGrade = "U"
print("You got a ", numberGrade, "% on your ",testName," exam, which is a ",letterGrade,".",sep='')
