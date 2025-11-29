print(""" 
1.Addition
2.Subtraction
3.Multiplication
4.Division 
5.Exit
""")

while True:
    choice = input("Enter Your Choice: ")

    if choice == "1":
        try:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        print("Addition is", num1 + num2)

    elif choice == "2":
        try:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        print("Subtraction is", num1 - num2)

    elif choice == "3":
        try:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        print("Multiplication is", num1 * num2)

    elif choice == "4":
        try:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if num2 == 0:
            print("Cannot divide by zero!")
            continue

        print("Division is", num1 / num2) 

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")