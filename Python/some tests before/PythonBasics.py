# First Python Program
# Simple statement Hello World
# Strings closed inside single/double/triple quotes

print('Hello, World')

a = 20

# Python statements ends with the token NEWLINE \n We can extend the statement over multiple lines using continuation
# character \ (doesn't affect white spaces)
# Implicit continuation to write a multi line statement, add continuation
# statement inside to treat as a single statement
addition = 10 + 20 + \
           30 + 40 + \
           50 + 60 + 70

addition2 = (10 + 20 +
             30 + 40 +
             50 + 60 + 70)

print(addition)

# Semicolumn ; to separate multiple statements (statement1 ; statement2)
l = 2
b = 6

print('Area of rectangle:', l * b)

# Indentation = 4 white spaces group of statements (block of code) (preceded by a colon : on previous line)
# If-else statement

num1 = 50
num2 = 100
if num1 > num2:
    print(num1, 'is greater than', num2)
elif num2 > num1:
    print(num2, 'is greater than', num1)
else:
    print('Both numbers are equal')

num1 = 500
if num1 > 100:
    if num1 % 2 == 0:
        print('Even number is greater than 100')

x = 20
print(x)

# list of strings
names = ['Emma',
         'Kelly',
         'Jessa']
print(names)

# dictionary name as a key and mark as a value
# string:int
students = {'Emma': 70,
            'Kelly': 65,
            'Jessa': 75}
print(students)

# Compound statements (groups of other statements; they affect or control the execution of those other statements in
# some way)
