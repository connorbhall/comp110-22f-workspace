from random import randint 

question: str = input("Ask a yes/no question... ")
response: int = randint(0, 4)

if response == 0:
    print("Yes, definitely")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("Fo Shizzle my Nizzle")
elif response == 3:
    print("hellllll nahhhh")
else:
    print("My sources say no")