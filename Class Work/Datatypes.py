#Data Types
#1.Numeric Types
#a.int
a=10
print(a)#10
print(type(a))#<class 'int'>
#b.Float
b=1.2
print(b)#1.2
print(type(b))#<class 'float'>
#c.complex
c=5+2j
print(c)#(5+2j)
print(type(c))#<class 'complex'>

#2. Sequence Types
#a. str
a="Python"
print(a)#Python
print(type(a))#<class 'str'>
#b. list
cart_items = ["phone","Laptop","Headphones"]
print(cart_items)#['phone', 'Laptop', 'Headphones']
print(type(cart_items))#<class 'list'>
#c. tuple
warehouse_location=(10.7733,22.8855)
print(warehouse_location)#(10.7733, 22.8855)
print(type(warehouse_location))#<class 'tuple'>

#3. Set Type
#a. Set
available_sizes={"S","M","L","XL","XXL"}
print(available_sizes)#{'XXL', 'L', 'S', 'XL', 'M'}
print(type(available_sizes))#<class 'set'>
#b. frozenset
frozen_tags=frozenset(["price","rice","ice"])
print(frozen_tags)#frozenset({'ice', 'price', 'rice'})
print(type(frozen_tags))#<class 'frozenset'>

#4. Mapping Type
#a. dict
product_details={"name":"phone","brand":"oppo","price":12000,"rating":4.6}
print(product_details)#{'name': 'phone', 'brand': 'oppo', 'price': 12000, 'rating': 4.6}
print(type(product_details))#<class 'dict'>

#5. Boolean Type
is_logged_in=True
is_payment_successful=False
is_in_stock=True
print(is_logged_in)#True
print(is_payment_successful)#False
print(is_in_stock)#True

#6. None Type
tracking_number=None
delivery_partner=None
print(tracking_number)#None
print(delivery_partner)#None
