#1.Square of a number using lambda
square = lambda n:n*n
print(square(4))
print(square(9))
#16
#81

#2.Check if number is even using lambda
trueorfalse = lambda n:"True" if n%2==0 else "False"
print(trueorfalse(12))
print(trueorfalse(13))
#True
#False

#3.Maximum of two numbers using lambda
maximumoftwo = lambda a,b: a if a>b else b
print(maximumoftwo(4,9))
print(maximumoftwo(7,3))
#9
#7

#4.Multiply two numbers using lambda
multiof2 = lambda a,b: a*b
print(multiof2(5,2))
#10

#5.sort a list of tuple by second element using lamba
l=[(1,3),(2,1),(4,2)]
sorted(l,key=lambda i:i[0])
print(sorted(l))

#[(1, 3), (2, 1), (4, 2)]

#6.Filter even numbers from a list using lambda and filter()
l=[1,2,3,4,5,6,7,8,9,10]
evenlist=list(filter(lambda i:i%2==0,l))
print(evenlist)
#[2, 4, 6, 8, 10]

#7.
l=[1,2,3,4,5,6,7,8,9]
squ=list(map(lambda i:i*i,l))
print(squ)
#[1, 4, 9, 16, 25, 36, 49, 64, 81]

#8
name=["hello","world"]
uppername = list(map(lambda i:i.upper(),name))
print(uppername)
#['HELLO', 'WORLD']

#9
sort_by_age = lambda lst: sorted(lst, key=lambda x: x['age'])
print(sort_by_age([{'name': 'A', 'age': 30}, {'name': 'B', 'age': 20}]))
print(sort_by_age([{'age': 25}, {'age': 18}]))


#10
length = lambda s:len(s)
print(length("hello"))
#5

#11
vol = 'aeiouAEIOU'
check = lambda s:True if s[0] in vol else False
print(check)

#12
l = [1,2,3]
listup=list(map(lambda i:i+10,l))
print(listup)
#[11, 12, 13]

#13.
s=["a", "the", "lamp", "cat"]
update = list(filter(lambda i: len(i)>3,s))
print(update)

#14.
multiply_by_index = lambda lst: [x * i for i, x in enumerate(lst)]
print(multiply_by_index([1, 2, 3, 4]))
print(multiply_by_index([5, 6, 7]))

#15.
product_all = lambda lst: reduce(lambda a, b: a * b, lst)
print(product_all([1, 2, 3, 4]))
print(product_all([2, 5, 5]))


#16.Use lambda with filter to find multiples of 3
l=[1,3,4,6,9]
mulof3 = list(filter(lambda i:i%3==0 , l))
print(mulof3)

#17.
sort_by_length = lambda lst: sorted(lst, key=lambda x: len(x))
print(sort_by_length(["car", "elephant", "cat"]))
print(sort_by_length(["hi", "world", "python"]))

#18. Lambda to extract domain from email
extract_domain = lambda email: email.split('@')[1]
print(extract_domain("user@gmail.com"))
print(extract_domain("name@yahoo.com"))

#19.Use lambda to get last digit of a number
lastdg=lambda i:i%10
print(lastdg(123))
#3

#20. Use lambda to check if year is a leap year
is_leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap_year(2020), is_leap_year(2023))
