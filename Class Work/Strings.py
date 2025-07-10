s1="Hello"
s2="World"
s3="Kusuma"
print(s1)#Hello
print(s2)#World
print(s3)#Kusuma

#Operations
#1. Concatination
str1="kusuma"
str2="Latha"
result=str1+" "+str2
print(result)#kusuma Latha
#2. Repetition
print("Python!" * 4)#Python!Python!Python!Python!
#3. Indexing
text="Maheshkumar"
print(text[0])#M
print(text[-1])#r
#4. Slicing
print(text[0:4])#Mahe
print(text[:5])#Mahes
print(text[7:])#umar
#5. Membership
print('Mahesh' in text)#True
print('kusuma' not in text)#True
print('kumar' in text)#True

#Bult-in String Functions
#1. len()
text="My Father name is Kullayappa"
print(len(text)) #28
#2. max() and min()
print(max("xyzABC")) #z
print(min("xyzABC")) #A
#3. sorted()
print(sorted("india")) #['a', 'd', 'i', 'i', 'n']
#4. chr() and ord()
print(ord('K'))#75
print(chr(68))#D

#1. Case Conversion Methods
x="Python"
print(x.lower())#python
print(x.upper())#PYTHON
print(x.capitalize())#python
print(x.title())#python
print(x.swapcase())#PYTHON
print(x.casefold())#python

#2. Alignment & Formatting Methods
x="Operating System"
print(x.center(40,"*"))#************Operating System************
print(x.ljust(40,"-"))#Operating System------------------------
print(x.rjust(40,"#"))#########################Operating System
print("55".zfill(5))#00055

#3. Search & Find Methods
x="Hello"
print(x.find('1'))#-1
print(x.rfind('1'))#-1
print(x.index('e'))#1
print(x.rindex('o'))#4
print(x.count('l'))#2

#4. String Testing Methods
x="Kusumalatha"
print(x.startswith("Ku"))#True
print(x.endswith("ha"))#True
print(x.isalpha())#True
print(x.isalnum())#True
print(x.islower())#False
print(x.isupper())#False
print(x.isspace())#False
print(x.istitle())#True
print(x.isidentifier())#True
print(x.isdecimal())#False
print(x.isdigit())#False
print(x.isnumeric())#False

#5. Replace & Modify Methods
x="Kusumalatha"
print(x.replace("a","b"))#Kusumblbthb
print(x.translate(str.maketrans("a","x")))#Kusumxlxthx
print(x.maketrans("suma","$%*&"))#{115: 36, 117: 37, 109: 42, 97: 38}

#6. Splitting & Joining Methods
X="Kusumalatha Student"
print(x.split(","))#"Kusumalatha","Student"
print(x.rsplit(",",1))#['Kusumalatha']
x='''Kusumalatha
Best
Student'''
print(x.splitlines())#['Kusumalatha', 'Best', 'Student']
x=["Kusumalatha"," Student"]
print(''.join(x))#Kusumalatha Student
x="Kusumalatha-Student"
print(x.partition("-"))#('Kusumalatha', '-', 'Student')
print(x.rpartition("-"))#('Kusumalatha', '-', 'Student')

#7. Whitespace & Trimming Methods
x="Pythonlanguage"
print(x.strip())#Pythonlanguage
x="------Pythonlanguage"
print(x.lstrip("-"))#Pythonlanguage
x="Pythonlanguage---------"
print(x.rstrip("-"))#Pythonlanguage

#8. Encoding & Decoding Methods
y="Hello"
print(y.encode("utf-8"))#b'Hello'
y=b"hello"
print(y.decode("utf-8"))#hello