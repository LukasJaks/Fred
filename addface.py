print("Welcome to Fred Face Adder 1.0")
typed = ""
while(True):
    typed = input("To add face, select A to end, press E: ")
    if(len(typed) != 1):
        print("invalid option")
    else:
        if(typed in "Aa"):
            print("Face Added")
        elif(typed in "Nn"):
            break