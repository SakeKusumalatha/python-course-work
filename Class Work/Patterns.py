#PATTERNS

#1.
'''Enter the size: 5
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * * '''
n=int(input("Enter the size: "))
for j in range(n):
    for i in range(n):
        print("*",end=" ")
    print()

#2.
'''Enter the size: 5
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * * '''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print("*",end=" ")
    print()

#3.
'''Enter the size: 5
* * * * * 
* * * * *
* * * * *
* * * * *
* * * * * '''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print("*",end=" ")
    print()

#4.
''' Enter the size: 4
* 
* *
* * *
* * * * '''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    print()
 
#5.
''' Enter the size: 5
* * * * * 
* * * *
* * *
* *
* '''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n-row):
        print("*",end=" ")
    print()

#6.
''' Enter the size: 5
        * 
      * *
    * * *
  * * * *
* * * * * '''
n=int(input("Enter the size: "))
for row in range(n):
    for spc in range(n-row-1):
        print(" ",end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()

#7.
''' Enter the size: 6
* * * * * * 
  * * * * *
    * * * *
      * * *
        * *
          * '''
n=int(input("Enter the size: "))
for row in range(n):
    for spc in range(row):
        print(" ",end=" ")
    for col in range(n-row):
        print("*",end=" ")
    print()

#8.
''' Enter the size: 7
* 
* *
* * *
* * * *
* * *
* *
* '''
n=int(input("Enter the size: "))
for row in range(n):
    if row<=n//2:
        for col1 in range(row+1):
            print("*",end=" ")
    else:
        for col2 in range(n-row):
            print("*",end=" ")
    print()

#9.
''' Enter the size: 6
* * * * * * 
*         *
*         *
*         *
*         *
* * * * * * '''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#10.
''' Enter the size: 5
* * * * * 
*   *   *
* * * * *
*   *   *
* * * * * '''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#11.
''' Enter the size: 7
* * * * * * * 
          *
        *
      *
    *
  *
* * * * * * * '''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col+row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#12.
''' Enter the size: 7
*           * 
  *       *
    *   *
      *
    *   *
  *       *
*           * '''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==col or col+row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#13.
''' Enter the size: 5
* * * * * 
  *   *
    *
  *   *
* * * * * '''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1 or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

