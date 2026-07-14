def add(p,q):
    return p+q
def subtract( p, q):
    return p-q
def multiply(p, q):
    return(p * q)
def divide(p, q):
    return(p/q)
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = str(input("Select any one of the choice: "))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter another number: "))

if choice == 'add':
    print(num1, "+" , num2 ,"="  ,add(num1, num2))
if choice == " Subtract" :
    print(num1, "-" , num2 , "=",subtract(num1, num2) )
if choice == " Multiply" :
    print(num1, "-" , num2 , "=",multiply(num1, num2) )
if choice == " Divide" :
    print(num1, "-" , num2 , "=",divide(num1, num2) )
