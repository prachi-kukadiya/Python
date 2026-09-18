#elif ->if you want to take multiple conditions you can take elif.

marks=int(input("Enter your marks :-"))
print("Entered marks :-",marks)

if marks >=90:
    print("You have achieved A+ grade")

elif marks >=80:
    print("You have achieved A grade")

elif marks >=70:
    print("You have achieved B grade")

elif marks >=60:
    print("You have achieved C grade")

elif marks >=50:
    print("You have achieved D grade")

else:
    print("You are failed in exam, Better luck next time !")