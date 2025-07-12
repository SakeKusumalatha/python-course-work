L=[1,2,3,4,5]
print(type(L)) #<class 'list'>

#1. Creating Lists
#1.1 Empty List
list=[]
print(list) #[]

#1.2 List with Elements
l=[1,2,3,4,5,6]
print(type(l)) #<class 'list'>
l=['Book','Pen','Pencil','Bag']
print(type(l)) #<class 'list'>
l=[4,"Python",(1,2,3),{"Name:Kusuma","ROll no:111","Course:MCA"}]
print(type(l)) #<class 'list'>

#1.3 List with Nested Lists
nested_list=[[1,2,3,4,5],['a','b','c,','d'],["kusuma","Latha","suma"]]
print(type(nested_list)) #<class 'list'>

#2. Accessing Elements in a List
#2.1 Indexing(Positive & Nagative)
l=["Java","Python","DBMS","Data"]
print(l[0]) #Java
print([-1]) #Data
print(l[1]) #Python

#2.2. Slicing
l=[1,2,3,3,4,5,5,5,6,6,7,8,9,1]
print(l[1:5]) #[2, 3, 3, 4]
print(l[:4]) #[1, 2, 3, 3]
print(l[5:]) #[5, 5, 5, 6, 6, 7, 8, 9, 1]
print(l[-2:-6]) #[]
print(l[::-1]) #[1, 9, 8, 7, 6, 6, 5, 5, 5, 4, 3, 3, 2, 1]

#3. Modifying List
#3.1 Changing  Elements
l=[10,20,30,40,50]
l[2]=60
print(l) #[10, 20, 60, 40, 50]

#3.2 Adding Elements
l=[1,2,3,3,4,5,5,5,6,6,7,8,9,1]
l.append(10)
print(l) #[1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 1, 10]
l=[1,2,3,3,4,5,5,5,6,6,7,8,9,1]
l.insert(1,8)
print(l) #[1, 8, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 1]
l=[1,2,3,3,4,5,5,5,6,6,7,8,9,1]
l.extend([10.15])
print(l) #[1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 1, 10.15]

#3.3 Removing Elements
l=[1,2,3,3,4,5,5,5,6,6,7,8]
l.remove(5)
print(l) #[1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8]
l=[1,2,3,3,4,5,5,5,6,6,7,8]
l.pop(2) 
print(l) #[1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
l=[1,2,3,3,4,5,5,5,6,6,7,8]
l.pop()
print(l) #[1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7]
l=[1,2,3,3,4,5,5,5,6,6,7,8]
del l[3]
print(l) #[1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
l=[1,2,3,3,4,5,5,5,6,6,7,8]
l.clear()
print(l) #[]

#4. List Methods
#append
l=[1,2,3,3,4,5,5,5,6,6,7,8]
l.append(34)
print(l) #[1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 34]
#extend
l=[10,20,30,40,50]
l.extend([60,70])
print(l) #[10, 20, 30, 40, 50, 60, 70]
#insert
l=[10,20,30,40,50]
l.insert(3,70)
print(l) #[10, 20, 30, 70, 40, 50]
#Remove
l=[6,7,4,3,9,2,1]
l.remove(1)
print(l) #[6, 7, 4, 3, 9, 2]
#Pop
l=[6,7,4,3,9,2,1]
l.pop(2)
print(l) #[6, 7, 3, 9, 2, 1]
#Clear
l=[6,7,4,3,9,2,1]
l.clear()
print(l) #[]
#Index
l=[6,7,4,3,9,2,1]
print(l.index(4)) #9
#Count
l=[1,2,3,3,4,5,5,5,6,6,7,8]
print(l.count(5)) #3
#Sorted
l=[6,7,4,3,9,2,1]
l.sort()
print(l) #[1, 2, 3, 4, 6, 7, 9]
#Reverse
l=[1,2,3,4,5,6,7]
l.reverse() 
print(l) #[7, 6, 5, 4, 3, 2, 1]
#Copy
#shallow Copy
l=[1,2,3,3,4,5,5,5,6,6,7,8]
m=l.copy()
print(m) #[1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8]
#Deep Copy
l=[1,2,3,3,4,5,5,5,6,6,7,8]
n=l
n.append(100)
print(n) #[1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 100]

#5. Copying a List
#Shallow Copy
l=[11,22,33,44,55]
m=l.copy()
print(m) #[11, 22, 33, 44, 55]

#6. Sorting and Reversing List
#Sorting
l=[11,55,88,44,77]
l.sort()
print(l) #[11, 44, 55, 77, 88]
#Reverse
l=[1,2,3,4,5,6,7]
l.reverse()
print(l) #[7, 6, 5, 4, 3, 2, 1]


#7. Min and Max
#min
l=[3,66,44,76,24,100,198]
print(min(l)) #3
#max
print(max(l)) #198
#Sum
l=[2,4,6,8,10]
print(sum(l)) #30
#Len
l=[1,2,3,4,5,6,7,8]
print(len(l)) #8
#Any
l=[1,2,3,4,5,6,7]
print(any(l)) #True
#All
l=[1,2,3,4,5,6,7]
print(all(l)) #True




