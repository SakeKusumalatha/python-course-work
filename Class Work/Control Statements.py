#Control Statements

#1. For Loop Statements
seats={
    "U1":{'price':1029,'booking_status':True},
    "U2":{'price':1029,'booking_status':False},
    "U3":{'price':1029,'booking_status':True},
    "U4":{'price':1029,'booking_status':False},
    "L1":{'price':2029,'booking_status':True},
    "L2":{'price':2029,'booking_status':False},
    "L3":{'price':2029,'booking_status':True},
    "L4":{'price':2029,'booking_status':True},
    
    }
for i in seats:
    if seats[i]['booking_status']:
        print(f'***{i}***')
    else:
        print(f'{i}-{seats[i]["price"]}') #***U1***,U2-1029,***U3***,U4-1029,***L1***,L2-2029,***L3***,***L4***.
seatno=input("Enter the seat no: ").upper()
if seatno in seats:
    if seats[seatno]['booking_status']:
     print(f'{seatno} is already booked. Go for the other one!!') #U1=U1 is already booked. Go for the other one!!
    else:
        name=input('Enter the name: ').title()
        age=int(input('Enter your age: '))
        gender=input('Enter your gender(F or M): ').upper()
        if age<=5:
            print(f'Hello {name} your seat booked successfully with free of cost.')# L2=Madhubala,4,F=Hello Madhubala your seat booked successfully with free of cost.
        elif age<15:
            print(f'Hello {name} your seat booked successfully with 50% discount\nTotal Price={seats[seatno]["price"]*0.5}')#L2=Pooja,14,F=Hello Pooja your seat booked successfully with 50% discount
        else:
            print(f'Hello {name} your seat booked successfull. Pay the amount-{seats[i]["price"]}')#L2=Mahesh,21,M=Hello Mahesh your seat booked successfull. Pay the amount-2029
else:
    print('Enter the seat no properly') #L5=Enter the seat no properly

#2. Break Statements

n=int(input("Enter the number: "))
isprime=False
for i in range(2,n//2+1):
    if n%i==0:
        isprime=True
        break
if isprime:
    print("Not a prime number") #45=Not a prime number
else:
    print("prime number") #19=prime number


#count value
    
n=int(input("Enter the number: "))
c=0
for i in range(2,n//2+1):
    if n%i==0:
        c=1
        break
if isprime:
    print("Not a prime number") #6=Not a prime number
else:
    print("prime number") #5=prime number

#3. COntinue Statements
# Print odd numbers only
for num in range(1,10):
    if num%2==0:
        continue
    print(num) #1,3,5,7,9

#4. While Loop Statements
#4.1 example
moves=24
winningpoint=int(input("Enter the winning point: "))
while moves>0:
    if moves==winningpoint:
        print("Congrats!!! You Won the game")
        break
    print(f"{moves} are left.You have chance to win the game")
    moves-=1
else:
    print("Game Over.Try again")
#OUTPUT:
#Enter the winning point: 10
#24 are left.You have chance to win the game
#23 are left.You have chance to win the game
#22 are left.You have chance to win the game
#21 are left.You have chance to win the game
#20 are left.You have chance to win the game
#19 are left.You have chance to win the game
#18 are left.You have chance to win the game
#17 are left.You have chance to win the game
#16 are left.You have chance to win the game
#15 are left.You have chance to win the game
#14 are left.You have chance to win the game
#13 are left.You have chance to win the game
#12 are left.You have chance to win the game
#11 are left.You have chance to win the game
#Congrats!!! You Won the game

#4.2 Example:
s='Python programming'
ind=0
n=len(s)
while ind<n:
    print(s[ind])
    ind+=1
#OUTPUT:
#P
#y
#t
#h
#o
#n

#p
#r
#o
#g
#r
#a
#m
#m
#i
#n
#g


#4.3 Example:
n=3
while n<19:
    print(n)
    n=n+3
#OUTPUT:
#3
#6
#9
#12
#15
#18

