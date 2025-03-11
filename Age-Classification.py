Age = int(input("what is your age?:"))
if Age < 0:
    print("invalid input, try again")
elif Age < 13:
    print("you are a child")
elif Age < 20:
    print("you are a teenager")
elif Age < 65:
    print("you are an adult")
elif Age >65:
    print("you are a senior")
    


