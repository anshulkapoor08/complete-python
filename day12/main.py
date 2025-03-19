# string slicing
name = "Hii, Anshul Kapoor"
print(name[0:7]) #3 index is not included

fruit = "Mango"
len = len(fruit)
print(len)
print(fruit[0:len])
print(fruit[1:4]) #given last index is not inlucded 
print(fruit[:])

# negative slicing

print(fruit[-1]) #last character
print(fruit[-2]) #second last character
print(fruit[-2:]) #last two character
print(fruit[:-2]) #all character except last two character
print(fruit[0:-3]) #all character except last three character
print(fruit[-3:-1]) # it will looks like([(len)-3: (len)-1]) last three character except last one
# hence it looks like [2:4] so it will print 3rd and 4th character

# start marking from behind with -1 and so on and for dry run start from left to right

nm = "kapoor"
print(nm[-4:-2])