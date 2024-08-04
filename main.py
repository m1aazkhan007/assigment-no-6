
# List
# Question: Write a function that takes a list of integers
# and returns the sum of all the elements in the list.

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_of_list([3,5,8,10,17,31])) 

# Tuple
# Question: Write a function that takes a tuple of numbers
# and returns the smallest number in the tuple.

def smallest_number(*numbers):
    return min(numbers)
print(smallest_number(* (4,6,3,9,11,22)))


# Set
# Question: Write a function that takes a set of numbers
# and returns a new set with each element squared.

def set_numbers(*numbers):
    return {num**2 for num in numbers}

print(set_numbers(*{2,4,6,7,9,13}))

# Dictionary
# Question: Write a function that takes a dictionary
# and returns a list of all the keys in the dictionary.

def dic(person={
    "name":"M. Zeeshan",
    "Gender":"Male",
    "Age":"19",
    "City":"Karachi"
}):
    return list(person.keys())
print(dic())