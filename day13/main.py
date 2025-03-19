# strings are immuatble
a = "kapoor!!"
b = "anshul kapoor chaurasiya"
print(len(a))
print(a.upper()) #perform operation and return a new sting intead of modifying the original one
print(a.lower())
print(a.rstrip("!")) #remove trailing characters but if there is any leading charecters it will not remove
print(a.replace("kapoor!!", "Chaurasiya"))
print(b.split(" ")) #split the string into list of strings
blogheading = "python is awesome"
print(blogheading.capitalize())

str1 = "welcome to the console"
print(len(str1))
print(str1.center(50)) 

print(a.count("a")) #count the number of occurences of a substring in a string

print(a.endswith("!!"))#return bool value

print(str1.endswith("to", 4, 10))

str1 = "He's name is Kapoor. He is an honest person"
print(str1.find("iss")) #return the index of the first occurence of the substring if not then return -1

print(str1.index("is")) #return the index of the first occurence of the substring if not then return error

st2 = "a;nvaduh51"
print(st2.isalnum()) #return true if all the characters are alphanumeric

st3 = "1234"
print(st3.isalnum())

st4 = "anshul"
print(st4.isalnum())    