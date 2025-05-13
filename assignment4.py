# task 1 - list of fruits
fruits = ["stawberry", "raspberry", "mango", "cocount", "pomegranate"]

print("Original List: ", fruits)
# add new fruit
fruits.append("orange")
print("After adding a fruit: ", fruits)
# remove fruit
fruits.remove("mango")
print("After removing a fruit: ", fruits)
# reverse list
fruits.reverse()
print("Reversed list: ", fruits)
print()

# task 2 - dictionaries
my_dict = { "name" : "Mariyah", "age" : 19, "city" : "Los Angeles" }

# add favorite color
my_dict["favorite color"] = "green"

# change city
my_dict["city"] = "New York"

# print list using a loop
print("Final dictionary:")
print("Keys: ", end="")
for key in my_dict:
    print(key, end=", ")
print("\nValues: ", end="")
for value in my_dict.values():
    print(value, end=", ")

print()
print()

# task 3 - tuples
my_tuple = ("Talk to Me", "Snooze", "Normal People")
print("Favorite things: ", my_tuple)

# change second element
# my_tuple[1] = "Layers"
# print("After changing second element: ", my_tuple)
print("Oops! Tuples cannot be changed.")

print("Length of tuple: ", len(my_tuple))





