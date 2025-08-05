#1, Function data Formation:

data={'current_balance':5000,'history':[]}

def Menu():
    print('[c]heck Balence')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transaction History')
    print('[E]xit')

def Welcome():
    print('Welcome to ATM'.center(40,'*'))

def Check_Balance():
    print(f'Current Balance: ${data["current_balance"]}')

def Withdraw():
    amount=int(input("Enter the amount to withdraw: "))
    if amount<=data['current_balance']:
        data['current_balance']-=amount
        data['history'].append(f'Withdraw: ${amount}')
        print(f'${amount} is successfully Withdraw!!!')
    else:
        print('Insufficient Balence')
        
def Deposit():
    amount=int(input("Enter the awmount to deposit:"))
    data['current_balance']+=amount
    data['history'].append(f'Deposited: ${amount}')
    print(f'${amount} is successfully deposited!!!')

def View_History():
    if data['history']:
        print('Transaction History'.center(40,'-'))
        for i in data['history']:
            print(i)
        else:
            print("No Transaction")

def Flow_Check(ch):
    if ch=='C':
        Check_Balance()
    elif ch=='D':
        Deposit()
    elif ch=='W':
        Withdraw()
    elif ch=='V':
        View_History()
   
Welcome()
while True:
    Menu()
    ch=input("Enter the char[CDWVE]: ").upper()
    Flow_Check(ch)
    if ch=='E':
        print("Thankyou".center(40,'.'))
        break
else:
    print("Invalid Choice")

# OUTPUT:
'''*************Welcome to ATM*************
[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit
Enter the char[CDWVE]: D
Enter the awmount to deposit:100000
$100000 is successfully deposited!!!
[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit
Enter the char[CDWVE]: W 
Enter the amount to withdraw: 50000
$50000 is successfully Withdraw!!!
[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit
Enter the char[CDWVE]: V
----------Transaction History-----------
Deposited: $100000
Withdraw: $50000
No Transaction
[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit
Enter the char[CDWVE]: C
Current Balance: $55000
[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit
Enter the char[CDWVE]: V
----------Transaction History-----------
Deposited: $100000
Withdraw: $50000
No Transaction
[c]heck Balence
[D]eposit
[W]ithdraw
[V]iew Transaction History
[E]xit
Enter the char[CDWVE]: E
................Thankyou................'''
 

#2. Function Arguments:
# 2.1. Position Argument(agr):

def function_name(agr1,agr2,agr3):
    #block of code

 function_name(val1,val2,val3)
 function_name(val3,val1,val2)
 function_name(agr1,agr2,agr3)


def student_details(name,rollno,marks,grade,course):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
student_course=input("Course: ")

student_details(name,rollno,marks,grade,student_course)
student_details("xyz",65,100,'A','Java')
'''#Input:
Name: Kusuma
Roll no: 39
Marks: 86
Grade: A
Course: MCA
#Output:
Name: Kusuma
Rollno: 39
Marks: 86
Grade: A
Course: MCA
Name: xyz
Rollno: 65
Marks: 100
Grade: A
Course: Java'''

#2.2.Keyword Agr(Argument):

def function_name(agr1,agr2,agr3):
    #block of code

 function_name(agr1='val1',agr2='val2',agr3='val3')
 function_name(agr2='val1',agr1='val2',agr3='val3')

def student_details(name,rollno,marks,grade,course):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
student_course=input("Course: ")

student_details(name=name,rollno=rollno,marks=marks,grade=grade,course=student_course)

student_details(rollno=rollno,name=name,grade=grade,course=student_course,marks=marks)

student_details(rollno=56,name='ramya',grade='A',course='Mysql',marks=99)

'''#Input:
Name: Sowmya
Roll no: 003
Marks: 80
Grade: A
Course: MCA
#Output:
Name: Sowmya
Rollno: 3
Marks: 80
Grade: A
Course: MCA
Name: Sowmya
Rollno: 3
Marks: 80
Grade: A
Course: MCA
Name: ramya
Rollno: 56
Marks: 99
Grade: A
Course: Mysql'''

#2.3.Default Agr(Argument):
def function_name(agr1,agr2,agr3='val3'):
    #block of code

 function_name(val1,val2)
 function_name(val3,val1)
 function_name(agr1,agr2,agr3)


def student_details(name,rollno,marks=0,grade="F",course='Python'):
    print('Name:',name)
    print('Rollno:',rollno)
    print('Marks:',marks)
    print('Grade:',grade)
    print('Course:',course)

name=input("Name: ")
rollno=int(input("Roll no: "))
marks=int(input("Marks: "))
grade=input("Grade: ")
course=input("Course: ")

student_details(name,rollno)

student_details(name,rollno,marks)

student_details(name,rollno,marks,grade)

student_details(name,rollno,marks,grade,course)

'''#Input:
Name: Swathi
Roll no: 84
Marks: 90
Grade: A+
Course: MBA
Name: Swathi
Rollno: 84
Marks: 0
Grade: F
Course: Python
Name: Swathi
Rollno: 84
Marks: 90
Grade: F
Course: Python
Name: Swathi
Rollno: 84
Marks: 90
Grade: A+
Course: Python
Name: Swathi
Rollno: 84
Marks: 90
Grade: A+
Course: MBA'''


#2.4.Variable Lenght

def function_name(*agr):
    #block of code

 function_name(val1,val2,val3,val4)
 function_name(val3,val1)
 function_name(agr1,agr2,agr3)
 function_name(agr1)


def names(*stdnames):
    print("\nName of students")
    for i in stdnames:
        print(f"**{i.upper()}**")

names('kalyan','Adarsh','saikumar')
names('kalyan','Adarsh','saikumar','nihitha','keethana','leorah')
names('kalyan','nihitha','keethana','leorah')
names('Ramya','nihitha','keethana','leorah')
names('Ramya','nihitha','keethana','Sunitha','maheswari')

'''#Output:
Name of students
**KALYAN**
**ADARSH**
**SAIKUMAR**

Name of students
**KALYAN**
**ADARSH**
**SAIKUMAR**
**NIHITHA**
**KEETHANA**
**LEORAH**

Name of students
**KALYAN**
**NIHITHA**
**KEETHANA**
**LEORAH**

Name of students
**RAMYA**
**NIHITHA**
**KEETHANA**
**LEORAH**

Name of students
**RAMYA**
**NIHITHA**
**KEETHANA**
**SUNITHA**
**MAHESWARI**'''
def function_name(**agr):
    #block of code

 function_name(agr1='val1')
 function_name(agr2='val1',agr1='val2',agr3='val3')
 function_name(agr1='val2',agr3='val3')
 function_name(agr2='val1',agr1='val2',agr3='val3',agr4='val4')



def display_products(**product):
    print("\nProducts and Prices: ")
    for i in product:
        print(f'{i}: ${product[i]}')

display_products(laptop=60000,phone=35000,watch=15000,fridge=200000)
display_products(fashwash=600,perfume=2000,eyeliner=1500,powder=2500)
display_products(carrot=25,tomato=30,beetroot=40,apple=50)

'''#Output:
Products and Prices: 
laptop: $60000
phone: $35000
watch: $15000
fridge: $200000

Products and Prices: 
fashwash: $600
perfume: $2000
eyeliner: $1500
powder: $2500

Products and Prices: 
carrot: $25
tomato: $30
beetroot: $40
apple: $50'''



