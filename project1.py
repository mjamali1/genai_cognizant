# step 1
age = int(input("How old are you? "))

# step 2 & step 3
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
elif age > 0:  
    diff = 18 - age
    print("You are not eligible to vote yet. You have", diff, "years to go.")
else:
    print("Invalid age entered. Please rerun the program and try again.")
    
