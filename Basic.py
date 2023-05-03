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