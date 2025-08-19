#ATTRIBUTES AND CLASS :

class shopping:
    discount=10

    def myorder(self,order):
        self.order=order
        print(f"{self.order} order is successfully added")



kusuma=shopping()
sowmya=shopping()
swathi=shopping()


kusuma.myorder('phone')
sowmya.myorder('jeans')
swathi.myorder('handbag')
#Output:phone order is successfully added
#jeans order is successfully added
#handbag order is successfully added

#METHODS:

class shopping:
    discount=10
    def __init__(self,name):
        self.name=name
        self.order=[]

    def myorder(self,order):
        self.order.append(order)
        print(f"{self.order}! \nYour {self.order} is successfully added")

    @classmethod
    def updateDiscount(cls,newdiscount):
        cls.discount=newdiscount
        print(f'Updated discount: {cls.discount}')

    @staticmethod
    def Welcome():
        print("Welcome to E_cart.Have a great shopping time.")


Kusuma=shopping('Kusuma')
Sowmya=shopping('Sowmya')
Swathi=shopping('Swathi')


Kusuma.myorder('phone')
Sowmya.myorder('jeans')
Swathi.myorder('handbag')
Kusuma.myorder('earrings')
Sowmya.myorder('braclet')
Swathi.myorder('dress')

shopping.updateDiscount(15)
shopping.Welcome()


#CONSTRUCTOR:

class shopping:
    def __init__(self,username,phonenumber,password):
        self.username=username
        self.phonenumber=phonenumber
        self.password=password
        self.favs=[]
        self.orders=[]
        self.mycart=[]
        print(f"Welcome to Flipkart {self.username}. Enjoy the shopping")


kusuma=shopping('kusuma','9014462548','Kusuma123')
#Output:
# ['phone']! 
#Your ['phone'] is successfully added
#['jeans']! 
#Your ['jeans'] is successfully added
#['handbag']! 
#Your ['handbag'] is successfully added
#['phone', 'earrings']!
#Your ['phone', 'earrings'] is successfully added
#['jeans', 'braclet']!
#Your ['jeans', 'braclet'] is successfully added
#['handbag', 'dress']!
#Your ['handbag', 'dress'] is successfully added
#Updated discount: 15
#Welcome to E_cart.Have a great shopping time.
#Welcome to Flipkart kusuma. Enjoy the shopping    
    
