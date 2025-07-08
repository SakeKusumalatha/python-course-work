#1.Arithmetic operators.py
a=10
b=20
print('Addition(a+b):',a+b)#Addition(a+b): 30
print('subtraction(a-b):',a-b)#subtraction(a-b): -10
print('Multiplication(a*b):',a*b)#Multiplication(a*b): 200
print('Division(a/b):',a/b)#Division(a/b): 0.5
print('Floor Division(a//b):',a//b)#Floor Division(a//b): 0
print('Modulus(a%b):',a%b)#Modulus(a%b): 10
print('Exponential(a**b):',a**b)#Exponential(a**b): 100000000000000000000

#2.Comparision operators.py
c=26
d=53
print('Equal to(c==d):',c==d)#Equal to(c==d): False
print('Not Equal to(c!=d):',c!=d)#Not Equal to(c!=d): True
print('Graeter than(c>d):',c>d)#Graeter than(c>d): False
print('Less than(c,d):',c<d)#Less than(c,d): True
print('Greater than or Equal to(c>=d):',c>=d)#Greater than or Equal to(c>=d): False
print('Less than or Equal to(c<=d):',c<=d)#Less than or Equal to(c<=d): True

#3.Assignment operators.py
a=15
a+=15
print('Add & Assign(a+=5):',a)#Add & Assign(a+=5): 30
a-=15
print('Subtract & Assign(a-=5):',a)#Subtract & Assign(a-=5): 15
a*=15
print('Multiply & Assign(a*=5):',a)#Multiply & Assign(a*=5): 225
a/=15
print('Devide & Assign(a/=5):',a)#Devide & Assign(a/=5): 15.0
a//=15
print('Floor Devide & Assign(a//=5):',a)#Floor Devide & Assign(a//=5): 1.0
a%=15
print('Modulus & Assign(a%=5):',a)#Modulus & Assign(a%=5): 1.0
a**=15
print('Exponential & Assign(a**=5):',a)#Exponential & Assign(a**=5): 1.0

#4.Logical operators.py
x=20
y=30
print(x>5 and y<40)#True
print(x>15 or y<40)#True
print(not (x>10))#False

#5.Membership operators.py
#String 
Name="Kusumalatha"
print('K' in Name)#True
print('l' in Name)#True
print('s' in Name)#True

#List
list=['Telugu','English','Hindhi','Maths']
print('Telugu' in list)#True
print('Maths' in list)#True
print('Social' in list)#False
print('Science' in list)#False

#Tuple
t=(11,22,33,44,55)
print(11 in t)#True
print(55 in t)#True
print(77 in t)#False

#Set
s=('car','bike','auto')
print('car' in s)#True
print('auto' in s)#True
print('bus' in s)#False
print('train' in s)#False

#Dictionary
D={'Name':'Kusuma','course':'MCA','Roll no':'39'}
print('Name' in D)#True
print('Kusuma' in D)#False
print('course' in D)#True