# Basic arithmetic tasks using python
width = 15
height = 12.0
print(height/3)

#Try - Except
temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
except:
    temp = 5
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)

#Function
def computeBMI(height_cm:float, weight:float):
    height_m = height_cm / 100  # convert height from cm to meters
    bmi = weight / (height_m ** 2)  # calculate BMI using formula
    return bmi
bmi = computeBMI(168, 58.8)
print("BMI: ", bmi)

#Max Function
print(max('Hello Worlds'))
print(max('Hello worlds'))

#Find smallest value in list
smallest = None
count = 0
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print(count)
    count+=1    
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

#sep keyword
print('cats', 'dogs', 'mice', sep=',')

#if-elif-else statement
Jane=1996
Annie=1996
if Annie%4==0:
    print("Annie was born in a leap year")
elif Jane%4==0:
    print("Jane was born in a leap year")
else:
    print("None of them were born in a leap year")

#function default return None
def new_func():
    print("PYTHON FOR EVERYONE")
print(new_func())

#read-write files with open
with open("C:/Users/Acer/Desktop/portfolio/Example.txt", "r") as File1:
    lines = File1.readlines()
    print(type(lines))
    print(len(lines))



with open("C:/Users/Acer/Desktop/portfolio/Example.txt", "w") as File1:
    File1.write("\nWrite this on the text file\n")
    File1.write("\nWrite this on the text file\n")

#check directory
import os

current_dir = os.getcwd()
print(current_dir)