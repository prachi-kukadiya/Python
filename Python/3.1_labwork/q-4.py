num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
num3=int(input("Enter third number :"))

if num1>num2 and num1>num3:
    print(num1,"The first number is the largest.")
elif num3>num1 and num3>num2:
    print(num3,"The third number is the largest.")
else :
    print(num2,"The second number is the largest.")