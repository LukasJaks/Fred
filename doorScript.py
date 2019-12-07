import random

print("Welcome to this super project called Fred 1.0")

while(True):
    iscalled = input("is triggred?: ")

    if(len(iscalled) != 0):
        iscalled = ""
        ran = int(random.choice([1, 2]))
        if(ran == 1):
            print("Door succesfully opened")
        else:
            print("Door stays closed")