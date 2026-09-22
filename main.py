import func, time, os

# func.que(2,["ahoj","add"])
match(func.que(2,["Alright!","ahh. i dont want to play this."],"some info")):
    case 1:
        print("okay... you are probably home. right... okay start the 'horor game'!")
        time.sleep(5)
        match(func.que(2,["yea come outside and breath fresh air","nah lets stay at home and rest there"],"you have a very hard day in your job...i think it would be great to go outside")):
            case 1:
                print("\okay then. good choice over the other...")
                time.sleep(4)
                print("\nYour home is in the forest (typical for horror). You know a secret little path. You walk straight towards the path, you found it, and you walk on the path. But then you remember you forgot your phone at home and started seeing stars. Do you know what that means...")
                match(func.que(1,["go back home"],"what do you do now")):
                    case 1:
                        pass

            case 2:
                print("okay you survived you litle modnster does not like horor monster like me...")
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


        
