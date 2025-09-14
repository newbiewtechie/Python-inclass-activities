ht= float(input("Enter your height"))
wt= float(input("Enter your weight"))
bmi= wt/ (ht/100)
print(bmi)
if(bmi <=18.4):
    print("You are underweight")
elif(bmi <=24.9):
    print("You are healthy")
elif(bmi <= 29.9):
    print("You are overweight")
elif(bmi <= 34.9):
    print("You are severly overweight")
elif(bmi <= 39.9):
    print("You are obese")
else:
    print("You are severly obese")
