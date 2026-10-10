numbers = input("Enter comma-separated numbers: ")

# Convert the string into a list
list_ = numbers.split(",")

# Convert the list into a set
set_ = set(list_)

# Convert the list into a tuple
tuple_= tuple(list_)

# Display the results
print("List:", list_)
print("Set:", set_)
print("Tuple:",tuple_)