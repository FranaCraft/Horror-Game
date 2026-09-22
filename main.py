import func
from playsound import playsound
# func.que(2,["ahoj","add"])
match(func.que(2,["Alright!","ahh. i dont want to play this."],"some info")):
    case 1:
        pass
    case 2:
        match(func.que(2,["okay then. i want to play","i want to quit!"])):
            case 1:
                quit

        
