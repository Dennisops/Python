print("This is just a simple calculator")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
choice = input("Choose your operation \n"
               "1)Addition \n"
               "2)Subtraction \n"
               "3)Division \n"
               "4)Multiplication \n")
# Addition
if choice == "1":
    result1 = num1 + num2
    print(num1, "+", num2, "is", result1)
    # Subtraction
elif choice == "2":
    result2 = num1 + num2
    print(num1, "-", num2, "is", result2)
    # Division
elif choice == "3":
    result3 = num1 / num2
    remainder = num1 % num2
    print(num1, "/", num2, "is", result3)
    # Multiplication
elif choice == "4":
    result4 = num1 * num2
    print(num1, "*", num2, "is", result4)
else:
    print("You did not give a valid input. Please try again")
