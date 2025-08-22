# USING SUPER() METHOD:

class A:
    def print_(self):
        print("This the parent class-A")


class B(A):
    def print_(self):
        super().print_()
        print("This is child class-B")

class C(B):
    def print_(self):
        super().print_()
        print("This is grand child-C")


c=C()
c.print_()
#OUTPUT:
#This the parent class-A
#This is child class-B
#This is grand child-C

#MULTIPLE INHERITANCE WITH SUPER()and MRO

class A:
    def print_(self):
        print("This the parent class-A")


class B:
    def print_(self):
        print("This is child class-B")

class C(A,B):
    def print_(self):
        A.print_(self)
        B.print_(self)
        print("This is grand child-C")


c=C()
c.print_()
#OUTPUT:
#This the parent class-A
#This is child class-B
#This is grand child-C

# EXAMPLE OF INHERITANCE :

class Phone:
    def __init__(self,user):
        self.user=user
        print(f"\nHellow {self.user}.Welcome, Enjoy the below features!!!!")
        print("Call")
        print("SMS")
        print("Snake and ladder")
        print("Alarm")
        print("FM Radio")


class PhoneV1(Phone):
    def __init__(self,user):
        super().__init__(user)
        print("Camera")
        print("Bluetooth")
        print("Music")
        print("Maps")


class PhoneV2(PhoneV1):
    def __init__(self,user):
        super().__init__(user)
        print("Internet")
        print("Front Camera")
        print("Finger Print")
        print("Google")



class PhoneV3(PhoneV1):
    def __init__(self,user):
        print(f"\nHello {user}, This is the trail version")
        print("Payments")
        print("Updated OS")
        print("FaceId")

class PhoneV4(PhoneV2,PhoneV3):
    def __init__(self,user):
        PhoneV2.__init__(self,user)
        PhoneV3.__init__(self,user)
        print("Scanner")
        print("5G")
        print("ESIM")
        print("Fast Charging")

        
kusuma=Phone('kusuma')
sowmya=PhoneV1('sowmya')
swathi=PhoneV2('swathi')
madhu=PhoneV3('madhu')
mahesh=PhoneV4('mahesh')

#OUTPUT:
''' Hellow kusuma.Welcome, Enjoy the below features!!!!
Call
SMS
Snake and ladder
Alarm
FM Radio

Hellow sowmya.Welcome, Enjoy the below features!!!!
Call
SMS
Snake and ladder
Alarm
FM Radio
Camera
Bluetooth
Music
Maps

Hellow swathi.Welcome, Enjoy the below features!!!!
Call
SMS
Snake and ladder
Alarm
FM Radio
Camera
Bluetooth
Music
Maps
Internet
Front Camera
Finger Print
Google

Hello madhu, This is the trail version
Payments
Updated OS
FaceId

Hello mahesh, This is the trail version
Payments
Updated OS
FaceId
Internet
Front Camera
Finger Print
Google

Hello mahesh, This is the trail version
Payments
Updated OS
FaceId
Scanner
5G
ESIM
Fast Charging     '''       


