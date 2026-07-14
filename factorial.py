def factorial (x):
    '''this is recursion function to find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else :
        return x * factorial(x-1)
    
print(factorial.__doc__)
print("factorial of 5 is ", factorial(5))
print("factorial of 6 is ", factorial(6))
 
