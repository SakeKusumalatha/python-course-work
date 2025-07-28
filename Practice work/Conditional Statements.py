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

#7. Check if number is 3-digit
num = 123
if 100 <= num <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")

#8. Check if Charecter is vowel
Char = "a"
if Char.lower() in 'aeiouAeiou':
    print("vowel")
else:
    print("Not a vowel")

#9. Check Greatest of two numbers
a, b = 7, 9
if a > b:
    print(f"{a} is grater")
else:
    print(f"{b} is greater")

#10. Check smallest of two numbers
a, b = 3, 8
if a < b:
    print(f"{3} is smallest number")
else:
    print(f"{b} is smallest number")

#11. Check if number is zero
num = 0
if num == 0:
    print("number is zero")
else:
    print("nubers is not zero")

#12. Check if number is multiple of 10
num = 50
if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not amultiple of 10")

#13. Check if age is eligible to vote(18+)
age = 19
if age >= 18:
    print("eligible for vote")
else:
    print("Not eligible for vote")

#14. Check if number is between 1 and 100
num = 45
if 1 <= num <= 100:
    print("in range")
else:
    print("Out of range")

#15. check if number is square of another
a, b = 4, 2
if a == b ** 2:
    print(f"{a} is square of {b}")
else:
    print(f"{a} is not square of {b}")

#16. Check if two strings are equal
str1, str2 ="apple","apple"
if str1 == str2:
    print("strings are equal")
else:
    print("strings are not equal")

#17. Check if a number is prime
num = 7
if num >1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("prime number")
else:
    print("Not a prime number")

#18. Check if number is positive and even
num = 12
if num > 0 and num % 2 == 0:
    print("positive and even number")
else:
    print("not a positive and even number")

#19. Check if character is uppercase
ch = "A"
if ch.isupper():
    print("uppercase letter")
else:
    print("Not an uppercase letter")

#20. Check if temperature is hot(>30)
temp = 35
if temp > 30:
    print("It's hot")
else:
    print("Temperature is normal")
