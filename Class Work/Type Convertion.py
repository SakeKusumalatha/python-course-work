#Type conversions

#Converting from int
a=5
print(type(a)) #<class 'int'>
print(float(a)) #5.0
print(complex(a)) #(5+0j)
print(bool(a)) #True
print(str(a)) #5
#print(list(a)) #Error
#print(tuple(a)) #Error
#print(set(a)) #Error
#print(dict(a)) #Error

#Converting from float
b=3.6
print(type(b)) #<class 'float'>
print(int(b)) #3
print(complex(b)) #(3.6+0j)
print(bool(b)) #True
print(str(b)) #3.6
#print(list(b)) #Error
#print(tuple(b)) #Error
#print(set(b)) #Error
#print(dict(b)) #Error

#Converting from String
s='python'
print(type(s)) #<lass 'str'>
print(bool(s)) #True
print(list(s)) #['p','y','t','h','o','n']
print(tuple(s)) #('p','y','t','h','o','n')
print(set(s)) #{'p', 't', 'y', 'n', 'o', 'h'}
#print(dict(s)) #Error
#print(int(s)) #Error
#print(float(s)) #Error
#print(complex(s)) #Error

#Converting from list
l=[2,4,6,8]
print(type(l)) #<class 'list'>
print(str(l)) #[2, 4, 6, 8]
print(bool(l)) #True
print(list(l)) #[2, 4, 6, 8]
print(tuple(l)) #(2, 4, 6, 8)
print(set(l)) #{8, 2, 4, 6}
#print(dict(l)) #Error
#print(int(l)) #Error
#print(float(l)) #Error
#print(complex(l)) #Error

#Converting from tuple
t=(2,4,6,8)
print(type(t)) #<class 'tuple'>
print(str(t)) #(2, 4, 6, 8)
print(bool(t)) #True
print(list(t)) #[2, 4, 6, 8]
print(set(t)) #{8, 2, 4, 6}
#print(dict(t)) #Error
#print(int(t)) #Error
#print(float(t)) #Error
#print(complex(t)) #Error

#Converting from set
s={1,2,3,4}
print(type(s)) #<class 'set'>
print(str(s)) #{1, 2, 3, 4}
print(bool(s)) #True
print(list(s)) #[1, 2, 3, 4]
print(tuple(s)) #(1, 2, 3, 4)
#print(int(s)) #Error
#print(float(s)) #Error
#print(complex(s)) #Error
#print(dict(s)) #Error

#Converting from dictionary
d={2:4,1:3}
print(type(d)) #<class 'dict'>
print(str(d)) #{2: 4, 1: 3}
print(bool(d)) #True
print(list(d)) #[2, 1]
print(set(d)) #{1, 2}
#print(int(d)) #Error
#print(float(d)) #Error
#print(complex(d)) #Error

#Converting from boolean
bool=True
print(type(bool)) #<class 'bool'>
print(int(bool)) #1
print(float(bool)) #1.0
print(complex(bool)) #(1+0j)
print(str(bool)) #True
#print(bool(bool)) #Error
#print(list(bool)) #Error
#print(set(bool)) #Error
#print(tuple(bool)) #Error

#Converting dict to dict
d = [('name', 'Mahesh'), ('batch', '22'), ('subject', 'python')]
print(dict(d)) #{'name': 'Mahesh', 'batch': '22', 'subject': 'python'}

