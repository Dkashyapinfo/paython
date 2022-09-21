
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("")
    ask = input("Enter your choice:\n")
    # print(type(ask))


    # =============================== O P T I O N  1 =============================== #

    if ask == 1 or ask == "1" or ask == "Addition" or ask == "addition" or ask == "Add" or ask == "add":
        # num1 = int(input("Enter your first number:\n"))
        num1 = input("Enter your first number:\n")
        while num1 == '':
            print("Please enter a number")
            print("")
            num1 = input("Enter your first number:\n")
        
        # num2 = int(input("Enter your second number:\n"))
        num2 = input("Enter your second number:\n")
        while num2 == '':
            print("Please enter a number")
            print("")
            num2 = input("Enter your second number:\n")
        # ans = int(num1)+int(num2)
        print("======================")
        print(num1 + " + " + num2 + " = " + "" + str(int(num1)+int(num2)))
        print("======================")
        print("")
    



    # =============================== O P T I O N  2 =============================== #

    elif ask == 2 or ask == "2" or ask == "Subtraction" or ask == "subtraction" or ask == "Subtract" or ask == "subtract":
        # num1 = int(input("Enter your number to be subtracted from:\n"))
        # num2 = int(input("Enter your number to be subtracted:\n"))
        # print(num1-num2)
        # num1 = int(input("Enter your first number:\n"))


        # ================== N U M  1 ==================== #

        num1 = input("Enter your number to be subtracted from:\n")
        while num1 == '':
            print("Please enter a number")
            print("")
            num1 = input("Enter your number to be subtracted from:\n")
        

        # ================== N U M  2 ==================== #

        # num2 = int(input("Enter your number to be subtracted:\n"))
        num2 = input("Enter your number to be subtracted:\n")
        while num2 == '':
            print("Please enter a number")
            print("")
            num2 = input("Enter your number to be subtracted:\n")
        # ans = int(num1)-int(num2)
        print("======================")
        print(num1 + " - " + num2 + " = " + "" + str(int(num1)-int(num2)))
        print("======================")
        print("")




    # =============================== O P T I O N  3 =============================== #

    elif ask == 3 or ask == "3" or ask == "Multiplication" or ask == "multiplication" or ask == "Multiply" or ask == "multiply":
        # num1 = int(input("Enter your first number:\n"))
        # num2 = int(input("Enter your second number:\n"))
        # print(num1*num2)

        # ================== N U M  1 ==================== #

        num1 = input("Enter your first number:\n")
        while num1 == '':
            print("Please enter a number")
            print("")
            num1 = input("Enter your first number:\n")
        

        # ================== N U M  2 ==================== #

        # num2 = int(input("Enter your second number:\n"))
        num2 = input("Enter your second number:\n")
        while num2 == '':
            print("Please enter a number")
            print("")
            num2 = input("Enter your second number:\n")
        # ans = int(num1)*int(num2)
        print("======================")
        print(num1 + " x " + num2 + " = " + str(int(num1)*int(num2)))
        print("======================")
        print("")
    




    # =============================== O P T I O N  4 =============================== #

    elif ask == 4 or ask == "4" or ask == "Division" or ask == "division" or ask == "Divide" or ask == "divide":
        # num1 = int(input("Enter dividend:\n"))
        # num2 = int(input("Enter divisor:\n"))
        # print(num1/num2)

        # ================== N U M  1 ==================== #

        num1 = input("Enter dividend:\n")
        while num1 == '':
            print("Please enter a number")
            print("")
            num1 = input("Enter dividend:\n")
        

        # ================== N U M  2 ==================== #

        # num2 = int(input("Enter divisor:\n"))
        num2 = input("Enter divisor:\n")
        while num2 == '':
            print("Please enter a number")
            print("")
            num2 = input("Enter divisor:\n")
        # ans = int(num1)*int(num2)
        print("======================")
        print(num1 + " ÷ " + num2 + " = " + str(int(num1)/int(num2)))
        print("======================")
        print("")




    # =============================== O P T I O N  5 =============================== #

    elif ask==5 or ask=="5" or ask=="Exit" or ask == "exit":
        break

    # ========================= O P T I O N  I N V A L I D ========================= #

    else:
        print("You have entered invalid option. Please Try Again.")
        print("")

print("Thank you for using the calculator.")


    # elif ask == 5 or ask == "5" or ask == "" or ask == "" or ask == "" or ask == "":
    #     num1 = int(input("Enter :\n"))
    #     num2 = int(input("Enter :\n"))
    #     print(num1  num2)
