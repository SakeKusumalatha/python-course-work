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
