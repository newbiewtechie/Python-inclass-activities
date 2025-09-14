amount = int(input("enter the amount to be withdrawn"))
note1= amount//100
note2= (amount%100)//50
note3= ((amount%100)%50)//10
print("notes of 100 = ", note1)
print("notes of 50 =" , note2)
print("notes of 10 =", note3)
