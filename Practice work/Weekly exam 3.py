#1.
salary=float(input())
if salary<=250000:
    print("No tax")
elif 250001<=salary<=500000:
    print(salary*0.05)
elif 500001<=salary<=1000000:
    print(salary*0.3)
elif salary>1000000:
    print(salary*0.2)


#2.
people=int(input)
ticket_collection=0
for i in range(people):
    age=int(input))
    if age<5:
        ticket_collection+=0
    elif 5<=age<=18:
        ticket_colletion+=100
    elif 19<=age<=60:
        ticket_collection+=150
    elif age>60:
        ticket_collection+=120


#3.
units=int(input())
bill=0
if units<=100:
    bill=unit*1.5
elif 101<=units<=200:
    bill=101*1.5+(units-100)*2.5
elif 201<=units<=500:
    bill=100*1.5+100*2.5+(units-200)*4
elif units>500:
    bill=100*1.5+100*2.5+300*4+(units-500)*6
print(bill)


#4.
hours=int(input())
if hours<2:
    print(30)
elif hours==24:
    print(200)
elif 2<hours<24:
    print(30+(hours-2)*10)

#5.
product=input()
qua=int(input())
if qua==0:
    print(f"{product}:Out of stock")
elif 1<=qua<=10:
    print(f"{product}:Low stock")
elif 11<=qua<=50:
    print(f"{product}:In stock")
elif qua>50:
    print(f"{product}:Over stock")

#6.
n=int(input())
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=' ')
    print()


#7.
ch=int(input())
people=int(input())
if ch==1:
    print(people*500)
elif ch==2:
    print(people*1300)
elif ch==3:
    print(people*500)
else:
    print("Invalid choice")


#8.
amount=int(input())
if 0<amount<=999:
    discount+=0
elif 1000<=amount<=4999:
    discount=amount*0.05
elif 5000<=amount<=9999:
    discount=amount*0.1
elif amount>10000:
    discount=amount*0.15
print(amount-discount)


#9.
stored_pin=1234
for i in range(3):
    pin=int(input())
    if pin==stored_pin:
        print("Access Granted")
        break
else:
    print("Access Denied")


#10.
n=int(input())
b=input().split()
print("Total",n)
print(len(b))
print(n-len(b))