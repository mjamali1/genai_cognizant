import turtle

# main function
def menu():
    print("Welcome to the Recursive Artistry Program!")
    print("Please choose an option:")
    print("\t1. Calculate the factorial of a number")
    print("\t2. Find the nth fibonacci number")
    print("\t3. Draw a recursive fractal pattern")
    print("\t4. Exit")

    userInput = int(input("Please enter your choice: "))

    # while loop ensures that 4 ends the program
    while(userInput != 4):

        # make sure user input is valid
        if (userInput < 1 or userInput > 4):
            print("Invalid choice. Please try again.")

        # first menu option
        elif (userInput == 1):
            choice = int(input("Enter a number to find it's factorial: "))
            while choice < 0:
                choice = int(input("Please enter a positive number: "))
            factorial(choice)
            print("The factorial of", choice, "is", factorial(choice))
        
        # second menu option
        elif (userInput == 2):
            choice2 = int(input("Enter the position of the fibonacci number: "))
            while choice2 < 0:
                choice2 = int(input("Please enter a positive number: "))
            fibonacci(choice2)
            print("The " + str(choice2) + "th fibonacci number is", fibonacci(choice2))
        
        # third menu option
        elif (userInput == 3):
            print("Drawing a heart!")
            fractal_pattern()
        
        userInput = int(input("Please enter your next choice: "))
        
# factorial function - recursive
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# fibonacci function - recursive
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# fractal pattern function
def fractal_pattern():
    turtle.speed(3)
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.left(120)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.done()

# call the main function
menu()
    