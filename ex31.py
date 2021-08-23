# Exercise 31. Making Decisions

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("there's a giant bear here eating a cheese cake")
    print("What do yo do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
bear = input("> ")
if bear == "1":
    print("The bear eats your face off. Good job!")
elif bear == "2":
    print("The bear eats your legs off.")
else:
    print(f"Well, doing {bear} is probably better.")
    print("Bear runs away.")
    