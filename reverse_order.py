num = int(input("enter a number "))
temp = abs(num)
count = 0
while temp > 0:
    temp = temp // 10
    count+= 1
print(str(num) + " has " +str(count) + " digits ")