#Dictonary

#1. Dictonary
Student={"name":"Kusuma","Course":"MCA","Roll no":39,"Batch no":2025}
print(Student) #{'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025}
print(type(Student)) #<class 'dict'>

#2. Dictonary Operations

#2.1 Accessing Values
Student={"name":"Kusuma","Course":"MCA","Roll no":39,"Batch no":2025}
print(Student["name"]) #Kusuma
print(Student.get("Roll no")) #39
print(Student.get("city","Not Available")) #Not Available

#2.2 Adding and Updating Items
Student={"name":"Kusuma","Course":"MCA","Roll no":39,"Batch no":2025}
Student["age"]=23
Student["city"]="Anantapur"
print(Student) #{'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'age': 23, 'city': 'Anantapur'}

#2.3 Removing items From a Dictionary

#Using Pop()
Student={"name":"Kusuma","Course":"MCA","age":23,"Batch no":2025}
age=Student.pop("age")
print(age) #23
print(Student) #{'name': 'Kusuma', 'Course': 'MCA', 'Batch no': 2025}

#Using del()
Student={"name":"Kusuma","Course":"MCA","age":23,"Batch no":2025}
del Student["Course"]
print(Student) #{'name': 'Kusuma', 'age': 23, 'Batch no': 2025}

#Using popitem()
Student={"name":"Kusuma","Course":"MCA","age":23,"Batch no":2025}
Student.popitem()
print(Student) #{'name': 'Kusuma', 'Course': 'MCA', 'age': 23}

#Using clear()
Student={"name":"Kusuma","Course":"MCA","Roll no":39,"Batch no":2025}
Student.clear()
print(Student) #{}

#3. Dictonary Built-in Methods

#3.1 Dictionary Methods for Accessing Data
#dict.get(key,default)
Student={'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'age': 23, 'city': 'Anantapur'}
print(Student.get("name","Not Found")) #Kusuma

#dict.keys()
Student={'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'age': 23, 'city': 'Anantapur'}
print(Student.keys()) #dict_keys(['name', 'Course', 'Roll no', 'Batch no', 'age', 'city'])

#dict.values()
Student={'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'age': 23, 'city': 'Anantapur'}
print(Student.values()) #dict_values(['Kusuma', 'MCA', 39, 2025, 23, 'Anantapur'])

#dict.items()
Student={'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'age': 23, 'city': 'Anantapur'}
print(Student.items()) #dict_items([('name', 'Kusuma'), ('Course', 'MCA'), ('Roll no', 39), ('Batch no', 2025), ('age', 23), ('city', 'Anantapur')])

#3.2 Dictonary Methods for Adding and Updating Data
#dict.update(new_dict)
Student={"name":"Kusuma","Course":"MCA","Roll no":39,"Batch no":2025}
Student.update({"city":"America"})
print(Student) #{'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'city': 'America'}

#dict.setdefault(key,default)
Student={'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'city': 'America'}
print(Student.setdefault("city","Unkown")) #America

#3.3 Dictionary Methodscfor Removing Data
#dict.pop(key,default)
Student={"name":"Kusuma","Course":"MCA","age":23,"Batch no":2025}
age=Student.pop("age")
print(age) #23
print(Student) #{'name': 'Kusuma', 'Course': 'MCA', 'Batch no': 2025}

#del dict[key]
Student={"name":"Kusuma","Course":"MBA","age":23,"Batch no":2025}
del Student["Course"]
print(Student) #{'name': 'Kusuma', 'age': 23, 'Batch no': 2025}

#dict.popitem()
Student={"name":"Kusuma","Course":"MCA","age":23,"Batch no":2025}
Student.popitem()
print(Student) #{'name': 'Kusuma', 'Course': 'MCA', 'age': 23}

#dict.clear()
Student={"name":"Kusuma","Course":"MBA","Roll no":39,"Batch no":2025}
Student.clear()
print(Student) #{}

#4. Built-in Functions for Dictionaries
#4.1 len(dict)
Student={'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'age': 23, 'city': 'Anantapur'}
print(len(Student)) #6

#4.2 max(dict)
Student={'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'age': 23, 'city': 'Anantapur'}
print(max(Student)) #name

#4.3 Min(dict)
Student={'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'age': 23, 'city': 'Anantapur'}
print(min(Student)) #Batch no

#4.4 Sorted(dict)
Student={'name': 'Kusuma', 'Course': 'MCA', 'Roll no': 39, 'Batch no': 2025, 'age': 23, 'city': 'Anantapur'}
print(sorted(Student)) #['Batch no', 'Course', 'Roll no', 'age', 'city', 'name']


#5. Nested Dictionaries
Students={"Kusuma":{"age":23,"course":"MCA"},"Sowmya":{"age":22,"course":"MBA"}}
print(Students["Kusuma"]["course"]) #MCA
print(Students["Sowmya"]["age"]) #22


#6. Dictionary Comprehension
Squares={x:x*x for x in range(1,6)}
print(Squares) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

