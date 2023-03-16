print ("Number of classes held")
classes_held = int(input())
print ("Number of classes attended")
classes_attended = int(input())
atten = (classes_attended / classes_held) * 100
print ("Attendence is")
if atten >= 75:
  print ("You are allowed to sit in exam")
else:
  print ("Sorry, you are not allowed. Attend more classes from next time.")