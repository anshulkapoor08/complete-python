a = "1"
b = "5"
print(int(a)+int(b)) #explicit typecasting gives output 6
print(a+b) #implicit typecasting gives output 15 because of string concatenation

# implicit typecasting in python always goes for bigger data type
a = 1
b = 5.0
print(a+b)


