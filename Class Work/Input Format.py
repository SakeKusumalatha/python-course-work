#String input
name=input('enter your name: ') #Kusuma
print(name) #Kusuma

#Integer input
quantity=int(input('enter the number of items: ')) #4
print(quantity) #4

#Float input
price=float(input('enter the product price: ')) #350.80
print(price) #350.80

#Input as List(space-seperated)
names=input('enter employee names(space-seperated):').split() #Ku su ma
print(names) #['Ku', 'su', 'ma']

#Input as List(comma-seperated)
tags=input('enter tags(comma-seperated):').split(',') #hi,how,are
print(tags) #['hi', 'how', 'are']

#List of integers
marks=list(map(int,input('enter marks: ').split())) #75 85 87 70
print(marks) #[75, 85, 87, 70]

#List of Floats
weights=list(map(float,input('enter weights: ').split())) #40.2 52.1 56.3
print(weights) #[40.2, 52.1, 56.3]

#Tuple input
dimensions=tuple(map(int,input('enter length,width,height: ').split())) # 5 10 15
print(dimensions) #(5, 10, 15)

#Set input
selected_ids=set(map(int,input('enter selected image IDs: ').split())) #111 112 113
print(selected_ids) #{111, 112, 113}

#Dictionary input using eval()
profile=eval(input('enter user profile as a dictionary: ')) #{'name':'Kusuma','age':23,'role':'Student'}
print(profile) #{'name': 'Kusuma', 'age': 23, 'role': 'Student'}

#Multiple inputs with unpacking
username, password=input('enter username and password: ').split() #Mahesh maheshkumarsake@gmail.com
print('username:', username) #username: Mahesh
print('password:', password) #password: maheshkumarsake@gmail.com