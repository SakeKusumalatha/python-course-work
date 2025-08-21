
#INHERITANCE:

#SINGLE INHERITANCE:
#(This is The Example of Single Inheritance)
class A:
    def printa(self):
        print("This is parent class-A")



class B(A):
    def printb(self):
        print("This is child class-B")



b=B()
b.printa()
b.printb()

#OUTPUT:This is parent class-A
#This is child class-B


#MULTILEVAL INHERITANCE:
#(This is The Example of Multileval Inheritance)
class A:                                   
    def printa(self):
        print("This is parent class-A")

class B(A):
    def printb(self):
        print("This is child class: B->A")

class C(B):
    def printc(self):
        print("This is grand child class: C->B->A")


c=C()
c.printa()
c.printb()
c.printc()

#OUTPUT:
#This is parent class-A
#This is child class: B->A
#This is grand child class: C->B->A

#MULTIPLE INHERITANCE:
#(this is The Example of Multiple Inheritance)
class A:                                   
    def printa(self):
        print("This is the parent class: A")

class B:
    def printb(self):
        print("This is the parent class: B")

class C:
    def printc(self):
        print("This is  the parent class: C")

class D(A,B,C):
    def printd(self):
        print("This is the child class: D->A")

d=D()
d.printa()
d.printb()
d.printc()
d.printd()

#OUTPUT:
#This is the parent class: A
#This is the parent class: B
#This is  the parent class: C
#This is the child class: D->A


#HIERARCHICAL INHERITANCE:
#(this is The Example of Hierarchical Inheritance)
class A:                                   
    def printa(self):
        print("This is the parent class: A->(A,B,D)")

class B(A):
    def printb(self):
        print("This is the child class: B->A")

class C(A):
    def printc(self):
        print("This is  the child class: C->A")

class D(A):
    def printd(self):
        print("This is the child class: D->A")

d=D()
d.printa()
d.printd()

#OUTPUT:
#This is the parent class: A->(A,B,D)
#This is the child class: D->A
