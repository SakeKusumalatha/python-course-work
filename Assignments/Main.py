# main.py
import my_programs as mp

def menu():
    while True:
        print("\n------ FUNCTION MENU ------")
        print("1. Merge Two Dictionaries")
        print("2. Check Leap Year")
        print("3. Largest Prime Factor")
        print("4. Digital Root of a Number")
        print("5. Replace Word in String")
        print("6. Count Uppercase Letters")
        print("7. Count Lowercase Letters")
        print("8. Find Median of List")
        print("9. Find Even Numbers")
        print("10. Find Odd Numbers")
        print("0. Exit")
        print("----------------------------")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice == "1":
            mp.merge_two_dicts()
        elif choice == "2":
            mp.check_leap_year()
        elif choice == "3":
            mp.largest_prime_factor()
        elif choice == "4":
            mp.digital_root()
        elif choice == "5":
            mp.replace_word()
        elif choice == "6":
            mp.count_uppercase()
        elif choice == "7":
            mp.count_lowercase()
        elif choice == "8":
            mp.find_median()
        elif choice == "9":
            mp.find_even()
        elif choice == "10":
            mp.find_odd()
        else:
            print("Invalid choice! Please enter a number from 0–15.")


menu()

