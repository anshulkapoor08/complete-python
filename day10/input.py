a = input() 
# input() is a built-in function in python that is used to take input from the user.
# input() function always returns a string/character hence we have to pass that into a variable.

b = input("Enter your name: ")

print("input by user is:", a)

print("my name is", b) 

x = input("Enter first number: ")
y = input("Enter second number: ")
print("sum of two numbers is", x+y)
# The output will be the concatenation of two numbers because input() function returns a string and we are adding two strings.

# To get the sum of two numbers we have to convert the strings into integers. 

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# print("sum of two numbers is", x+y) or
# print("sum of two numbers is", int(x)+int(y))
# output will be 11