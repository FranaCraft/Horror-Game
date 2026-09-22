import func, time, os

# func.que(2,["ahoj","add"])
match(func.que(2,["Alright!","ahh. i dont want to play this."],"some info")):
    case 1:
        pass
    case 2:
        match(func.que(2,["okay then. i want to play","i want to quit!"],"Are you sure?!")):
            case 1:
                print("I forgive you...")
                time.sleep(1)
                print("For now...")
                time.sleep(1)
                print("Not for long...")
                time.sleep(0.1)
                quit
            case 2:
                print("youre not gonna be alone for so long")
                time.sleep(3)
                os.system("shutdown --now")


        
