person={
    "name":"Alice",
    "age":25,
    "city":"New York"
}

print("Personal info :",person)

person["height"] = 5.9
print("After adding:", person)

person["age"] = 26
print("After updating age:", person)

del person["city"]
print("After removing city:", person)


