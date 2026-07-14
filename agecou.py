
try:
    age= int(input("Enter your age: "))
    if age%2 == 0:
        print("The age is valid and its even number")
    else:
        print("The age is valid and its odd number")
except ValueError:
    print("The age is invalid")


