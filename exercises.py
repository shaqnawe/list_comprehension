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
# print(sort_by_last(authors))

# Question 3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
# Created a function to convert from Celsius to Farenheit
def convert():
    # change temp from Celsius to Farenheit for second element of each item
    new_temps = lambda data: (data[0], data[1]*(9/5)+32)
    return new_temps
# create new list and execute a map function
print(list(map(convert(),places)))

# Question 4
# Write a recursive function that returns the fibonacci sequence up to the number passed in.
fibonacci_cache = {}
def fibonacci(num):
    # Base case to check for 0 and 1
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        # return the sum of num-1 and num-2 and save to value
        value = fibonacci(num-1) + fibonacci(num-2)
        # Save the value in fibonacci_cache dictionary for future reference
        # Prevents the program from computing the same numbers
        fibonacci_cache[num] = value
        return value

# print(fibonacci(9))