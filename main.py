name = input("What is your name?: ")
while name == "":
    name = input("What is your name?: ")
    if name == "":
        print("invalid input")
    else: 
        print(f"You name is {name}")