#1. Pasitive or Nagative
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Nagative number")
else:
    print("Zero")

#2. Even or Odd
num = int(input("Enter a number"))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#3. Divisible by 5
num = int(input("Enter a number"))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

#4. Divisible by 3 and 7
num = int(input("enter a number"))
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by 3 and 7")
else:
    print("Not Divisible by 3 and 7")

#5. Check for Leap Year
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a Leap Year")

#6. Check Pass or Fail
marks = int(input("Enter a number"))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

