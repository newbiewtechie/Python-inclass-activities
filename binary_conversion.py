num = int(input("Enter a decimal number: "))

binary = ""
temp = num

if num == 0:
    binary = "0"
else:
    while temp > 0:
        remainder = temp % 2
        binary = str(remainder) + binary
        temp = temp // 2

print("Binary equivalent:", binary)
