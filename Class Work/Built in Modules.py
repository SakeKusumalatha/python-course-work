#BUILT IN MODULES:

#SYS-Modules
#1.
import sys
print(sys.argv)
#output:['C:/Users/sakem/AppData/Local/Programs/Python/Python313/Built in module.py']

#2.
import sys

print(sys.path)
#Output:
['C:/Users/sakem/AppData/Local/Programs/Python/Python313', 'C:\\Users\\sakem\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\idlelib',
 'C:\\Users\\sakem\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'C:\\Users\\sakem\\AppData\\Local\\Programs\\Python\\Python313\\DLLs',
 'C:\\Users\\sakem\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\sakem\\AppData\\Local\\Programs\\Python\\Python313',
 'C:\\Users\\sakem\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']

#3.
import sys

print(sys.version)
#Output:3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)]

#4.
import sys

print("Befor exit")
print(sys.exit())
print("After exit")
#Output:3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)]

#Platform Modules:

import platform

print(platform.system())#Windows
print(platform.release())#11
print(platform.processor())#AMD64 Family 23 Model 104 Stepping 1, AuthenticAMD


#Math Modules:

import math

print(math.pi)#3.141592653589793
print(math.e)#2.718281828459045

print(math.sqrt(25))#5.0
print(math.pow(3,3))#27.0


print(round(12.3))#12
print(round(12.8))#13

print(math.ceil(12.3))#13
print(math.ceil(12.8))#13
print(math.ceil(12.0001))#13

print(math.floor(12.3))#12
print(math.floor(12.999999))#12

print(abs(-13))#13
print(abs(-12.4))#12.4

print(math.fabs(-13))#13.0
print(math.factorial(5))#120
print(math.gcd(8,12))#4

print(math.log(2))#0.6931471805599453
print(math.log(2,2))#1.0
print(math.sin(45))#0.8509035245341184
print(math.cos(45))#0.5253219888177297
print(math.tan(45))#1.6197751905438615

print(math.degrees(45))#2578.3100780887044
print(math.radians(45))#0.7853981633974483

#random Modules:

import random
random.seed(10)
print(random.random())#0.5714025946899135
print(random.randint(1,10))#7
print(random.uniform(1,5))#2.9302466982034234
l=['kusuma','sowmya','revathi','swathi','megana']
print(random.choice(l))#kusuma
print(random.choices(l,k=2))#['sowmya', 'megana']
print(l)#['kusuma', 'sowmya', 'revathi', 'swathi', 'megana']
random.shuffle(l)
print(l)#['megana', 'swathi', 'kusuma', 'sowmya', 'revathi']


#itertools:

from itertools import combinations,permutations

s='kusuma'
t=tuple(combinations(s,3))
for i in t:
    print(''.join(i),end=',')
#Output:kus,kuu,kum,kua,ksu,ksm,ksa,kum,kua,kma,usu,usm,usa,uum,uua,uma,sum,sua,sma,uma

#
from itertools import combinations,permutations

s='abc'
t=tuple(combinations(s,3))
p=tuple(permutations(s,3))

for i in t:
    print(''.join(i),end=',')
for i in p:
    print(''.join(i),end=',')
#Output:abc,abc,acb,bac,bca,cab,cba,


