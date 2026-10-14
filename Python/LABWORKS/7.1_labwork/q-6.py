# list of numbers

numbers=[10,20,30,40]


print("Original list :",numbers)

numbers.append(50)
print("After adding :",numbers)

numbers.remove(10)
print("After removing :",numbers)

numbers[2] = 25
print("After replacing :",numbers)


# tuple of numbers

tuple_numbers=(10,20,30,40,50)
print("Original tuple numbers",tuple_numbers)

# tuple_numbers[1] = 40

# A list is mutable, it can be added, removed, or changed after the list is created.
# But a tuple is immutable, it cannot be added, removed, or changed after the tuple is created.