# task 1

try:
    number = float(input("Enter a number: "))
    result = 100 / number
    print("100 divided by", number, "is", result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
print()

# task 2

# index error
try:
    my_list = [1, 2, 3]
    print(my_list[5])  
except IndexError:
    print("IndexError occurred! List index is out of range.")

# key error
try:
    my_dict = {"name": "Mar"}
    print(my_dict["age"])  
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# type error
try:
    result = "Hello" + 5  
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

print()

# task 3

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("The result is", result)
finally:
    print("This block always executes.")
