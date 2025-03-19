# Match case statement
p = int(input("enter the value of x:"))
match p:
    case 1:
        print("one")
    case _ if p!=1:
        print("two")
    case 3:
        print("three")
    case _:
        print(p)