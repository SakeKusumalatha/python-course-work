#1. Printr Numbers from 1 to N(Using for loop)
N = int(input("Enter N: "))
for i in range(1, N + 1):
    print(i, end=' ')

#2. Print Even Numbers from 1 to N(Using for loop)
N = int(input("Enter N: "))
for i in range(2, N + 1, 2):
    print(i, end=' ')

#3. Sum of Numbers from 1 to N(using for loop)
N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1):
    total += i
print("Sum:", total)

#4. Print Odd Numbers from 1 to N(Using for loop)
N = int(input("Enter N: "))
for i in range(1,N + 1,2):
    print(i,end=' ')

#5. Find Factorial of a Number(Using for loop)
N = int(input("Enter N: "))
fact = 1
for i in range(1, N + 1):
    fact *= i
print("Factorial:", fact)

#6. Print Multiplication Table of N(Using for loop)
N = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{N} X {i} = {N * i}")

#7. Check Prime Number
N = int(input("Enter a number: "))
is_prime = True
if N <= 1:
    is_prime = False
else:
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            is_prime = False
            break
if is_prime:
    print("prime")
else:
    print("Not prime")

#8. sum of Digit of a Number
n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n = n // 10
print("sum of digits:", sum_digits)

#9. Print Fibonacci Sequence up to N Terms
N = int(input("Enter number of terms: "))
a, b =0, 1
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b

#10. Count Numbers Divisible by 3
N = int(input("enter a number: "))
count = 0
for i in range(1, N + 1):
    if i % 3 == 0:
        count += 1
print("count of numbers divisible by 3:",count)

#11. Check if a number is Palindrome
n = int(input("enter a number: "))
original = n 
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#12. Print Multiples of 5 up to N
N = int(input("Enter a number: "))
for i in range(5, N + 1, 5):
    print(i, end=" ")

#13. Find the Maximun of Three Numbers
a = int(input("Enter first number: "))
b = int(input("enter second number: "))
c = int(input("Enter third number: "))
max_val = a
for num in [b, c]:
    if num > max_val:
        max_val = num
print("Maximum number is:", max_val)

#14. Print Reverse of a Number
 n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Reversed number:", reverse)

#15. Sum Of First N Natural Numbers
N = int(input("Enter a number: "))
total = 0 
for i in range(1, N + 1):
    total += i
print("Sum of first", N, "natural numbers is:", total)

#16. Print Numbers from N to 1
N = int(input("enter a number: "))
while N >= 1:
    print(n, end=" ")
    N -= 1

#17. Find Sum of Prime Numbers up to N
N = int(input("enter a number: "))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        return True
    total = 0
    for i in range(2, N + 1):
        if is_prime(i):
            total += i
print("Sum of prime numbers:", total)

#18. Find the Product of Digits of a number
n = int(input("enter a number: "))
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
print("Product of digits:", product)

#19. Print Numbers Divisible by Both 3 and 5
N = int(input("Enter a number: "))
for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")

#20. Find GCD of Two Numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second numbers: "))
while b != 0:
    a, b = b, a % b
print("GCD is:", a)

#21. Print Right-Angled triangle Pattern
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print("*" * i)

#22. Print Hollow Square Patten
n = int(input("Enter size of square: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#23. Check if a Number is Perfect
n = int(input("Enter a number: "))
sum_divisors = 0
for i in range(1, n):
    if n % i == 0:
        sum_divisors += i
if sum_divisors == n:
    print("Perfect")
else:
    print("Not Perfect")

#24. Count Digits in a Number
n = int(input("Enter a Number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("count of digits:", count)

#25. Print Numbers Divisible by 7
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 7 == 0:
        print(i, end=" ")

#26. Find the LCM of Two numbers
a = int(input("enter first number: "))
b = int(input("enter second number: "))
lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm %b == 0:
        print("LCM is:", lcm)
        break
    lcm += 1

#27. Print Even numbers in REverse Order
n = int(input("Enter a number: "))
while n >= 1:
    if n % 2 == 0:
        print(n, end=" ")
    n -= 1

#28. Sum of First N Odd Numbers
n = int(input("Enter a number: "))
sum_odd = 0
odd = 1
for i in range(n):
    sum_odd += odd
    odd += 2
print("Sum of first", N, "odd numbers is:",sum_odd)

#29. Print a Square Pattern of Numbers
n = int(input("Enter size of square: "))
for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()

#30. Check if a Number is Armstrong
n = int(input("Enter a Number: "))
num_str = str(n)
power = len(num_str)
sum_arm = 0
for digit in num_str:
    sum_arm += int(digit) ** power
if sum_arm == n:
    print("Armstrong")
else:
    print("Not Armstrong") 