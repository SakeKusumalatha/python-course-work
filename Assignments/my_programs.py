# my_programs.py

# 1. Merge Two Dictionaries
def merge_two_dicts():
    print("Program: Merge Two Dictionaries")
    print("""
def merge_dicts(d1, d2):
    d1.update(d2)
    return d1
""")
    print(" Test Case 1: merge_dicts({'a':1}, {'b':2}) → {'a':1, 'b':2}")
    print(" Test Case 2: merge_dicts({1:10}, {2:20}) → {1:10, 2:20}")
    print(" Explanation: Uses Python’s dict.update() method to merge two dictionaries.")

# 2. Check Leap Year
def check_leap_year():
    print("Program: Check Leap Year")
    print("""
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
""")
    print(" Test Case 1: is_leap_year(2020) → True")
    print(" Test Case 2: is_leap_year(1900) → False")
    print(" Explanation: Leap year rule: divisible by 4, but not 100, unless also divisible by 400.")

# 3. Largest Prime Factor
def largest_prime_factor():
    print("Program: Largest Prime Factor")
    print("""
def largest_prime_factor(n):
    factor = 2
    while n > 1:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return factor
""")
    print(" Test Case 1: largest_prime_factor(13195) → 29")
    print(" Test Case 2: largest_prime_factor(49) → 7")
    print(" Explanation: Repeatedly divides the number by factors until the largest prime factor remains.")

# 4. Digital Root of a Number
def digital_root():
    print("Program: Digital Root")
    print("""
def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n
""")
    print(" Test Case 1: digital_root(942) → 6")
    print(" Test Case 2: digital_root(57) → 3")
    print(" Explanation: Keeps summing digits until only one digit remains.")

# 5. Replace Word in a String
def replace_word():
    print("Program: Replace Word in String")
    print("""
def replace_word_in_string(s, old, new):
    return s.replace(old, new)
""")
    print(" Test Case 1: replace_word_in_string('I like apples','apples','oranges') → 'I like oranges'")
    print(" Test Case 2: replace_word_in_string('Python is fun','fun','awesome') → 'Python is awesome'")
    print(" Explanation: Uses string.replace() to substitute a word.")

# 6. Count Uppercase
def count_uppercase():
    print("Program: Count Uppercase Letters")
    print("""
def count_upper(s):
    return sum(1 for c in s if c.isupper())
""")
    print(" Test Case 1: count_upper('Hello') → 1")
    print(" Test Case 2: count_upper('WORLD') → 5")
    print(" Explanation: Iterates over characters and counts uppercase ones.")

# 7. Count Lowercase
def count_lowercase():
    print("Program: Count Lowercase Letters")
    print("""
def count_lower(s):
    return sum(1 for c in s if c.islower())
""")
    print(" Test Case 1: count_lower('Hello') → 4")
    print(" Test Case 2: count_lower('WORLD') → 0")
    print(" Explanation: Iterates over characters and counts lowercase ones.")

# 8. Find Median of List
def find_median():
    print("Program: Find Median")
    print("""
def median(lst):
    lst = sorted(lst)
    n = len(lst)
    if n % 2 == 1:
        return lst[n//2]
    else:
        return (lst[n//2 - 1] + lst[n//2]) / 2
""")
    print(" Test Case 1: median([3,1,2]) → 2")
    print(" Test Case 2: median([1,2,3,4]) → 2.5")
    print(" Explanation: Sorts the list and finds the middle element(s).")

# 9. Find Even Numbers
def find_even():
    print("Program: Find Even Numbers in List")
    print("""
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]
""")
    print(" Test Case 1: even_numbers([1,2,3,4]) → [2,4]")
    print(" Test Case 2: even_numbers([5,7]) → []")
    print(" Explanation: Uses list comprehension to filter even numbers.")

# 10. Find Odd Numbers
def find_odd():
    print("Program: Find Odd Numbers in List")
    print("""
def odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]
""")
    print(" Test Case 1: odd_numbers([1,2,3,4]) → [1,3]")
    print(" Test Case 2: odd_numbers([2,4,6]) → []")
    print(" Explanation: Uses list comprehension to filter odd numbers.")


#OUTPUT:
'''------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 1
Program: Merge Two Dictionaries

def merge_dicts(d1, d2):
    d1.update(d2)
    return d1

 Test Case 1: merge_dicts({'a':1}, {'b':2}) → {'a':1, 'b':2}
 Test Case 2: merge_dicts({1:10}, {2:20}) → {1:10, 2:20}
 Explanation: Uses Python’s dict.update() method to merge two dictionaries.

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 2
Program: Check Leap Year

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

 Test Case 1: is_leap_year(2020) → True
 Test Case 2: is_leap_year(1900) → False
 Explanation: Leap year rule: divisible by 4, but not 100, unless also divisible by 400.

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 3
Program: Largest Prime Factor

def largest_prime_factor(n):
    factor = 2
    while n > 1:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return factor

 Test Case 1: largest_prime_factor(13195) → 29
 Test Case 2: largest_prime_factor(49) → 7
 Explanation: Repeatedly divides the number by factors until the largest prime factor remains.

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 4
Program: Digital Root

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

 Test Case 1: digital_root(942) → 6
 Test Case 2: digital_root(57) → 3
 Explanation: Keeps summing digits until only one digit remains.

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 5
Program: Replace Word in String

def replace_word_in_string(s, old, new):
    return s.replace(old, new)

 Test Case 1: replace_word_in_string('I like apples','apples','oranges') → 'I like oranges'
 Test Case 2: replace_word_in_string('Python is fun','fun','awesome') → 'Python is awesome'
 Explanation: Uses string.replace() to substitute a word.

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 6
Program: Count Uppercase Letters

def count_upper(s):
    return sum(1 for c in s if c.isupper())

 Test Case 1: count_upper('Hello') → 1
 Test Case 2: count_upper('WORLD') → 5
 Explanation: Iterates over characters and counts uppercase ones.

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 7
Program: Count Lowercase Letters

def count_lower(s):
    return sum(1 for c in s if c.islower())

 Test Case 1: count_lower('Hello') → 4
 Test Case 2: count_lower('WORLD') → 0
 Explanation: Iterates over characters and counts lowercase ones.

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 8
Program: Find Median

def median(lst):
    lst = sorted(lst)
    n = len(lst)
    if n % 2 == 1:
        return lst[n//2]
    else:
        return (lst[n//2 - 1] + lst[n//2]) / 2

 Test Case 1: median([3,1,2]) → 2
 Test Case 2: median([1,2,3,4]) → 2.5
 Explanation: Sorts the list and finds the middle element(s).

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 9
Program: Find Even Numbers in List

def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

 Test Case 1: even_numbers([1,2,3,4]) → [2,4]
 Test Case 2: even_numbers([5,7]) → []
 Explanation: Uses list comprehension to filter even numbers.

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 10
Program: Find Odd Numbers in List

def odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

 Test Case 1: odd_numbers([1,2,3,4]) → [1,3]
 Test Case 2: odd_numbers([2,4,6]) → []
 Explanation: Uses list comprehension to filter odd numbers.

------ FUNCTION MENU ------
1. Merge Two Dictionaries
2. Check Leap Year
3. Largest Prime Factor
4. Digital Root of a Number
5. Replace Word in String
6. Count Uppercase Letters
7. Count Lowercase Letters
8. Find Median of List
9. Find Even Numbers
10. Find Odd Numbers
0. Exit
----------------------------
Enter your choice: 0
Exiting program. Goodbye!
'''

