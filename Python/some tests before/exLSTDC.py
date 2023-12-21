# Lists
# Collection which is ordered and changeable.
# Allows duplicates

# Create the list
my_list = [1, 2, 3, 4, 5]

# Append a new element
my_list.append(6)

# Access elements
print(my_list[0])   # First element
print(my_list[-1])  # Last element

# Slicing
print(my_list[1:4])  # Elements with index 1 to 3

# Length of a list
print(len(my_list))

# Exercises

fav_fruits = ['banana', 'ananas', 'zmeura', 'afine', 'piersici']

print(fav_fruits)
fav_fruits.append('mar verde')
print(fav_fruits[-1])
fav_fruits.remove('mar verde')
print(fav_fruits)
print(fav_fruits[1], fav_fruits[3])

numbers = [1, 2, 3, 4, 5]

doubled = [n * 2 for n in numbers]
print(doubled)

n10 = [num for num in range(1, 11)]
print(n10)
sqn10 = [sq ** 2 for sq in n10]
print(sqn10)
oeven = [number for number in n10 if number % 2 == 0]
print(oeven)

# Sets
# Unordered collection
# NO duplicates

my_set = {1, 2, 3, 4, 5}
print(type(my_set))
my_set.add(6)
print(my_set)
my_set.remove(1)
print(my_set)
print(3 in my_set)
print(len(my_set))
my_set.add(4)
print(my_set)

favColors = {'bllue', 'red', 'yellow', 'orange'}
print('blue' in favColors)
print(favColors)
favColors.remove('bllue')
favColors.add('blue')
favColors.add('black')
print(favColors)

# Tuples
# Collection is ordered and Unchangeable
my_tuple = (1, 2, 3)

print(my_tuple)
print(len(my_tuple))

difftuplle = (11, 'tiger', True)
print(difftuplle[0], difftuplle[-1])

# Dictionaries
# Collection which is unordered, changeable and indexed
my_dict = {"name": "Hector", "age": 30}

# Access items
print(my_dict["name"])

# Change value
my_dict["age"] = 31

# Add new key-value pair
my_dict["dict"] = "New York"
print(my_dict)

book = {'title': "48 Laws of Power", "author": "Robert Greene", "year": 1998}
book["genre"] = "self-dev"
book["year"] = "2023"
print(book)