#conditional Statements

#1. simple if Statement
age = int(input("Enter your age: ")) #Enter your age: 18
if age >=18:
    print("You are eligible to vote.") #You are eligible to vote.

#2. if-else Statement
password = input("Enter the password: ")
if password == "2468":
    print("Access granted.") #2468=Access granted.
else:
    print("Access denied.") #1234=Access denied.

#3. if-elif-else Statement
signal = input("Enter traffic light color red/yellow/green): ").lower()
if signal == "red":
    print("Stop!") #red=Stop!
elif signal == "yellow":
    print("Get ready to go.") #yellow=Get ready to go.
elif signal == "green":
    print("Go!") #green=Go!
else:
    print("Invalid signal color.")

#4. Nested Conditional Statements
distance = float(input("Enter your home distance form school(in km):"))
class_grade = int(input("Enter your class grade: "))
if distance >3:
    if class_grade>=6:
        print("You are eligiblefor the school bus.") #7=You are eligiblefor the school bus.
    else:
        print("Only students from class 6 and above are eligible.") #5=Only students from class 6 and above are eligibl
else:
    print("You live too close to need the school bus.") #6=You live too close to need the school bus.

#5. Nested-if
hr,mins=list(map(int,input('enter the HH:MM :').split(':')))
if hr>=0 and hr<=24 and mins>=0 and mins<=60:
    if hr>=0 and hr<4:
        print('Its high time.Time to sleep') #02:15=Its high time.Time to sleep
    if hr>=4 and hr<12:
        print('Good morning.Have a nice day') #10:30=Good morning.Have a nice day
    if hr>=12 and hr<16:
        print('Good afternoon.Have a great lunch') #14:20=Good afternoon.Have a great lunch
    if hr>=16 and hr<20:
        print('Good evening.Have some snacks') #19:05=Good evening.Have some snacks
    if hr>=20 and hr<24:
        print('Good night.Sweet dreams') #21:39=Good night.Sweet dreams
else:
    print('Enter the proper input,Your input is invalid')
