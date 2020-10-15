#1 somethings not right
a = 0
if a > 1 and a < 10:
    print("A is between 1 & 10") 

#2 These statements are supposed to all true if it prints.
a = 10
b = "Bob"

if a >= 10:
    print("a is greater or equal to 10")
    if b == "Bob":
        print("Bobs the name and as is 10 or more")
    elif b != "bob":
        print("Bob is not the name and a is 10.")
else:
    print("a is less than 10.")
