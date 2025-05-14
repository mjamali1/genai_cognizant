# step 4 - logging errors

import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

# step 1
def menu():

    # print intro statemnts
    print("Welcome to the Error-Free Calculator!")
    choice = input("Choose an operation: \n\t1. Addition \n\t2. Subtraction \n\t3. Multiplication \n\t4. Division \n\t5. Exit\n")

    # loop until user chooses to exit
    while choice != "5":
        if choice == "1":
            calculate("add")
        elif choice == "2":
            calculate("subtract")
        elif choice == "3":
            calculate("multiply")
        elif choice == "4":
            calculate("divide")
        else:
            print("Invalid choice. Please try again.")
        choice = input("Choose an operation: \n\t1. Addition \n\t2. Subtraction \n\t3. Multiplication \n\t4. Division \n\t5. Exit\n")
    
    # exit message
    print("Goodbye!")

# step 2 & 3

def calculate(operation):

    try:
        # get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # perform the operation
        if operation == "add":
            print("Result:", num1 + num2)
        elif operation == "subtract":
            print("Result:", num1 - num2)
        elif operation == "multiply":
            print("Result:", num1 * num2)
        elif operation == "divide":
            try:
                result = num1 / num2
                print("Result:", result)
            # division error
            except ZeroDivisionError:
                print("Oops! Division by zero is not allowed.")
                logging.error("ERROR:root:ZeroDivisionError occurred: division by zero")
    # value error
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        logging.error("ERROR:root:ValueError occurred: invalid input.")
    # finally block
    finally:
        print("Thank you for using the calculator!")

# run the program
menu()