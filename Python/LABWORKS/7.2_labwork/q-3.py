numbers = int(input("Enter a number you want to add : "))

numberList=[]

for i in range(numbers):
    num=int(input(f"Enter number {i + 1} : "))
    numberList.append(num)



print("Number list",numberList)

uniquevalues=set(numberList)
print("Unique values",uniquevalues)
