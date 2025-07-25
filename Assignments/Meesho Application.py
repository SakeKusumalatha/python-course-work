# Meesho-like Product Information System

# Task 1: Take Product Details as Input
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
categories = input("Enter Categories (comma-separated): ").split(',')

available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)

discount_percentage = float(input("Enter Discount Percentage: "))

features_input = input("Enter Product Features (comma-separated): ")
product_features = set(feature.strip() for feature in features_input.split(','))

supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}

# Task 2: Display Product Details Using Different Formatting Methods

# 1. Comma Separation (sep=',')
print("\n--- Output using Comma Separation ---")
print("Product ID, Name, Price:", product_id, product_name, price, sep=',')

# 2. Percentage Formatting
print("\n--- Output using Percentage Formatting ---")
print("Product Discount: %.2f%%" % discount_percentage)

# 3. f-strings
print("\n--- Output using f-strings ---")
print(f"Product Name: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount_percentage}%")
print(f"Stock Available: {stock_details[0]} units")
print(f"Categories: {', '.join(categories)}")
print(f"Features: {', '.join(product_features)}")

# 4. .format() method
print("\n--- Output using .format() method ---")
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(
    supplier_details["Name"],
    supplier_details["Contact"],
    supplier_details["Location"]
))

#INPUT DETAILS:

#Enter Product ID: 101
#Enter Product Name: Kusuma
#Enter Price: 300
#Enter Categories (comma-separated): Electronic,Cloths
#Enter Available Stock: 50
#Enter Sold Stock: 20
#Enter Discount Percentage: 10.0
#Enter Product Features (comma-separated): Water proof,Longlastin battery
#Enter Supplier Name: Meesho
#Enter Supplier Contact Number: 1236544896
#Enter Supplier Location: Ap

#OUTPUT:

#--- Output using Comma Separation ---
#Product ID, Name, Price:,101,Kusuma,300.0

#--- Output using Percentage Formatting ---
#Product Discount: 10.00%

#--- Output using f-strings ---
#Product Name: Kusuma
#Price: ₹300.0
#Discount: 10.0%
#Stock Available: 50 units
#Categories: Electronic, Cloths
#Features: Longlastin battery, Water proof

#--- Output using .format() method ---
#Supplier Details: Name - Meesho, Contact - 1236544896, Location - Ap

