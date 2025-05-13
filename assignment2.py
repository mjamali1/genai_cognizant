# task 1 - countdown
starting_number = int(input("Enter the starting number: "))

while starting_number > 0:
    print(starting_number, end=' ')
    starting_number -= 1

print("Blast off!")
print()

# task 2 - multiplication table
number = int(input("Enter a number: "))
print()

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
print()

# task 3 - factorial
num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("The factorial of", num, "is", factorial)
