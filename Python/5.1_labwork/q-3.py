name=input("Enter your name : ")

print(f"Entered name : {name}")

palindrome= name[::-1]

if palindrome==name:
    print("Given name is palindrome.")
else:
    print("Given name is not palindrome.")