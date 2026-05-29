year=int(input("Enter the year:"))
if (year%4==0):
    print("Leap year")
elif(year%400==0):
    print("Leap year")
elif(year%100==0):
    print("Leap year")
else:
    print("Not a leap year")

#2 
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#3 ternary 
year = int(input("Enter year: "))
print("Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year")

#Function
def is_leap(year):
    return(year % 4==0 and year % 100 !=0) or (year%400==0)
year=int(input("Enter the year:"))
if is_leap(year):
    print("Leap year")
else:
    print("Not Leap year")
