tdays= int(input("enter total number of days = "))
year= tdays//365
week= (tdays%365)//7
days= ((tdays%365)%7)
print("Number of years= ", year, "\nNumber of weeks= ", week, "\nNumber of days = ", days)

