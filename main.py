import Resources.func as func,time,Resources.res as res,random
lines = []
until_next_thng = 3 + random.randint(-2,5)
for ch_counter in range(until_next_thng):
    if random.randint(1,2) == 1:
        func.display_image(res.crossroadx4)
        match(func.key(4)):
            case 1:
                func.display_image(res.crossroadx4_left)
            case 2:
                func.display_image(res.crossroadx4_str)
            case 3:
                func.display_image(res.crossroadx4_right)
            
                
    else:
        func.display_image(res.crossroadx3)
        match(func.key(3)):
            case 1:
                func.display_image(res.crossroadx3_left)
            case 2:
                func.display_image(res.crossroadx3_right)
    
    func.keyboard.wait("enter")
    print("jej")
        