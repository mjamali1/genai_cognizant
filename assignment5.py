# task 1

def greet_user(name):
    print("Hello, " + name + "! Welcome Aboard.")

def add_numbers(a, b):
    return a + b


greet_user("Mar")
print("The sum of 5 and 3 is " + str(add_numbers(5, 3)) + ".")

# task 2

def describe_pet(pet_name, animal_type="dog"):
    print("I have a " + animal_type + " named " + pet_name + ".")

print()
describe_pet("Marvin")
describe_pet("Sweetie", "cat")


# task 3

def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients: ", end="")
    for ingredient in ingredients:
        print("-", ingredient, end=" ")

print()
make_sandwich("Turkey", "Cucumber", "Lettuce")


# task 4

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testing Task 4
print()
print("\nFactorial of 4 is", factorial(4))
print("The 8th Fibonacci number is", fibonacci(8))
