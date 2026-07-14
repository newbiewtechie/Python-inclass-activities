amount= float(input("Enter the amount of the bill: "))
paid= float(input("Enter the amount you paid: "))
due= amount- paid
if due>0:
    print("You need to pay RS ", due, " to the shopkeeper")
elif due<0:
    print("You need RS", abs(due), " from the shopkeeper")
else:
    print("The bill payment is done")
