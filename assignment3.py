# task 1 - string slicing
str = "Python is amazing!"

print("Original String:", str)
print() 
# print first word
print("First word:", str[:6])       
# print amazing     
print("Amazing part:", str[10:17]) 
# print reversed
print("Reversed string:", str[::-1])   
print()

# task 2 - string methods
str2 = " hello, python world! "

print("Original String:", str2)
print()

str2 = str2.strip()  
print("After strip():", str2)

str2 = str2.capitalize()
print("After capitalize():", str2)

str2 = str2.replace("world", "universe")
print("After replace():", str2)

str2 = str2.upper()
print("After upper():", str2)

print() 

# task 3 - palindrome checker
word = input("Enter a word: ").strip()

# Checking if the word is a palindrome
if word == word[::-1]:
    print("Yes,", word, "is a palindrome!")
else:
    print("No,", word, "is not a palindrome!")
