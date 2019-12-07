print("Welcome to Fred Face Adder 1.0")
ttyped = ""
while(True):
    ttyped = input("To add face, select A to end, press E: ").upper()
    if(len(ttyped) != 1):
        print("invalid option")
    else:
        if(ttyped == "A"):
            print("Face Added")
        elif(ttyped == "E"):
            break

