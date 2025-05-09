
# task 1 -- introduce myself

name = "Mariyah"
age = 19
height = 5.2

print("Hi everyone, my name is " + name + "! I am " + str(age) + "years old but my birthday is coming up. My height is " + str(height) + " feet.")
print()
# task 2 -- arithmetic 

num1 = 27
num2 = 4

# addition
print("The sum of 27 and 4 is", (num1 + num2))
# subtraction
print("The difference of 27 and 4 is ", (num1 - num2))
# multiplication
print("The product of 27 and 4 is ", (num1 * num2))
# division
print("The division of 27 and 4 is ", (num1 / num2))
print()

# task 3 -- conditional statements

# ask user to enter a number
num = int(input("Please enter a number: "))

if num > 0:
    print("The number is positive. Awesome!")
elif num < 0:
    print("The number is negative. Better luck next time!")
else:
    print("The number is zero. Perfect balance!")
