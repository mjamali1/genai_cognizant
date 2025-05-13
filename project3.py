password = input("Enter a password: ")
print()

score = 0

# constrants:
# length >= 8 (2 points)
# at least one uppercase letter (2 points)
# at least one lowercase letter (2 points)
# at least one digit (2 points)
# at least one special character (2 points)
# 10 points max.

# check length
if len(password) >= 8: 
    score += 2
else:
    print("Password should be at least 8 characters long.")

# check for uppercase letters
if any(char.isupper() for char in password):
    score += 2
else:
    print("Password should include at least one uppercase letter.")

# check for lowercase letters
if any(char.islower() for char in password):
    score += 2
else:
    print("Password should include at least one lowercase letter.")

# digits
if any(char.isdigit() for char in password):
    score += 2
else:
    print("Password should include at least one digit.")

# special characters
if any(not char.isalnum() for char in password):
    score += 2
else:
    print("Password should include at least one special character.")

# Output results
if score == 10:
    print("Your password is strong!")
else:
    print("Your password could be stronger:")

print()
print("Password score:", score, "/10")
