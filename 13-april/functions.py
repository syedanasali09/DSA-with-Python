def name():
    name= input("Enter your Name:")
    print(name,"syedanasali09")
name()

def add():
    number1= int(input("Number 1 is:"))
    number2 = int(input("Number 2 is:"))
    sum = number1+number2
    print("Sum of two numbers is:", sum)
add()

def difference():
    number1= int(input("Number 1 is:"))
    number2 = int(input("Number 2 is:"))
    result = number1-number2
    print("Difference of two numbers is:", result)
difference()

def myFruits(f1, f2, f3, f4):
    FruitsList = [f1, f2, f3, f4]
    return FruitsList
output = myFruits("Apple", "Bannana", "Grapes", "Orange")
print(output)

def myChocolates(cList):
    for i in cList:
        print(i)

chocolateList = ["Dairy Milk","Snickers","Kitkat"]
myChocolates(chocolateList)

def Calendar(year, month, date=''):
    print(year, month, date)
Calendar(2023, 2, 14)
