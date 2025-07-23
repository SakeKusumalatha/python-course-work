# ASSINGMENT:1

# MOVIE TICKET BOOKING APPLICATION

# Input Collection
movie_id = int(input("Enter Movie ID: "))
movie_name = input("Enter Movie Name: ")
ticket_price = float(input("Enter Ticket Price: "))
categories = input("Enter Categories (comma-separated): ").split(",")
available_seats = int(input("Enter Available Seats: "))
booked_seats = int(input("Enter Booked Seats: "))
gst_percent = float(input("Enter GST Percentage: "))
features = set(input("Enter Features (comma-separated): ").split(","))
theater_details = {
    "name": input("Enter Theater Name: "),
    "location": input("Enter Theater Location: "),
    "contact": input("Enter Theater Contact Number: ")
}

# 1. Comma Separation
print("\n--- Booking Summary ---")
print("Movie ID, Name, Price:", movie_id, movie_name, ticket_price, sep=",")

# 2. Percentage Formatting
print("GST Applied: %.2f%%" % gst_percent)

# 3. f-strings
print(f"\nMovie Name: {movie_name}")
print(f"Ticket Price: ₹{ticket_price}")
print(f"Seats Available: {available_seats}")
print(f"Seats Booked: {booked_seats}")
print(f"Categories: {', '.join([c.strip() for c in categories])}")
print(f"Features: {', '.join(features)}")

# 4. .format() method
print("\nTheater Details: Name - {}, Location - {}, Contact - {}".format(
    theater_details["name"], theater_details["location"], theater_details["contact"]
))

#INPUT DETAILS :

Enter Movie ID: 2026
Enter Movie Name: Salaar
Enter Ticket Price: 200.0
Enter Categories (comma-separated): Action,Thriller
Enter Available Seats: 150
Enter Booked Seats: 50
Enter GST Percentage: 20.0
Enter Features (comma-separated): 4K,Dobly Atmos
Enter Theater Name: PVR cinemas
Enter Theater Location: Hyderabad
Enter Theater Contact Number: 8106354715

#OUTPUT:
--- Booking Summary ---
Movie ID, Name, Price:,2026,Salaar,200.0
GST Applied: 20.00%

Movie Name: Salaar
Ticket Price: ₹200.0
Seats Available: 150
Seats Booked: 50
Categories: Action, Thriller
Features: 4K, Dobly Atmos

Theater Details: Name - PVR cinemas, Location - Hyderabad, Contact - 8106354715