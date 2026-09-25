try : 
   num1, num2 = eval(input("Enter two numbers, seperatde by a coma : "))
   result = num1/num2
   print("Result =", result)
except ZeroDivisionError :
   print ("Division by zero throws error")
except SyntaxError :
   print("Comma is missing. Enter numbers seperated by a comma")
except:
   print("wrong input")
else:
   print("No exceptions")
finally :
   print("This will excute no matter what")