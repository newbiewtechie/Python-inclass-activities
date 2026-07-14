def PerSq(x):
    per= x*4
    return(per)
def PerRec(a,b):
    per= a*b
    return(per)

z= int(input("Enter the sides of the Square: "))
print("Perimeter of Square is: ", PerSq(z))
p= int(input("Enter the length of the Rectangle: "))
q= int(input("Enter the breadth of the Rectangle: "))
print("Perimeter of Rectangle is: ", PerRec(p,q))

