#1 I need to add something to protect the program
#number = input("Give me a number between 1 and 10")
number = "Not A Number"
try:
    number = int(input)
except ValueError:
    print("You didn't give a number")

print("Great Job on giving me the NUMBER %s" % number)
