# Question 1
# Filter out all of the empty strings from the list below
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']

def remove_empty(places):
    for place in places:
        # Iterate each item and check if length > 0
        # and each item is not compose of spaces
        if len(place) != 0 and not place.isspace():
            return True
        else:
            return False
# create a new list and filter out all false values (empty strings and strings composed of only spaces)
new_list = list(filter(remove_empty,places))
print(new_list)
# filter out all empty strings and strings composed of only spaces but using filter and lambda
new_list = list(filter(lambda place: len(place) != 0 and not place.isspace(), places))
print(new_list)

# Question 2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
def sort_by_last(fn_list):
    full_names = []
    # Break the initial list of full names into indivial list items
    for author in fn_list:
        # Add to new list called full_names
        full_names.append(author.split())
    # print(full_names)
    last_name_sorted = []
    # iterate through each name in full_names and sort based on last name index[-1]
    # lower case so it doesn't throw off the last name starting with lower case chars
    for last in sorted(full_names, key=lambda x:x[-1].lower()):
        # add each name to last_name_sorted list and join names separating them with a space in-between
        last_name_sorted.append(' '.join(last))
    return last_name_sorted
print(sort_by_last(authors))

# Question 3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
f_temp = []
# Created a function to convert from Celsius to Farenheit
def convert():
    for i in places:
        # change temp from Celsius to Farenheit for second element of each item in the list
        new_temp = i[1]*(9/5)+32
        # Add the each city and new temp to new tuple
        f_temp.append((i[0],new_temp))
    return f_temp
# create new list and run lamdba function on each tuple
new_temps = list(map(lambda places:places,convert()))
print(new_temps)

# Question 4
# Write a recursive function that returns the fibonacci sequence up to the number passed in.

def fibonacci(num):
    # Base case to check for 0 and 1
    if num in [0,1]:
        # print(num)
        return num
    else:
        print(num)
        # return the sum of num-1 and num-2 recursively
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(10))
