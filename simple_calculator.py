while True:
    print("\n--Choose the Operation--")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    
    
    choice = int(input("Enter your choice: "))
    
    if choice == 5:
        print("Thanks for using Calculator!!")
        break
    else:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if choice == 1:
            print(f"Addition is: {a+b}")
        elif choice == 2:
            print(f"Subtraction is: {a-b}")
        elif choice == 3:
            print(f"Multiplication is: {a*b}")
        elif choice == 4:
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Division is: {a/b}")
        else:
            print("Invalid input!!!")
        
    
    