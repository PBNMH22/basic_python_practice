# this program is used for grading system
score=float(input("enter your score="))
if score>0 and score<1:
     
     if score>=0.9:
          print("you got A grade")
     elif score>=0.8:
          print("you got B grade")
     elif score>=0.7:
          print("you got C grade")
     elif score>=0.6:
          print("you got D grade")
     else:
          print("Study hard Dued...!")
else:
     print("please check your input")
