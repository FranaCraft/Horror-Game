
import Resources.func as func, Resources.res as res, random, Resources.playsound, time
intro = "You are Traped in Drainage System and maybe..."
intro2 = "...with you."
intro3 = "and you need to get out of here, but quick! because water level is rising!"
outro = "hey wait i see light!"
outro2 = "finally light. last ladder and iam out"

print(intro)
time.sleep(4)
print(intro2)
time.sleep(4)
print(intro3)
time.sleep(5)

until_next_thng = 3 + random.randint(-2,5)
for level in range(10):
    for ch_counter in range(until_next_thng):
        if random.randint(1,2) == 1:
            match(func.key(4, res.crossroadx4)):
                case 1:
                    func.display_image(res.crossroadx4_left)
                case 2:
                    func.display_image(res.crossroadx4_str)
                case 3:
                    func.display_image(res.crossroadx4_right)

                
                    
        else:
            match(func.key(3, res.crossroadx3)):
                case 1:
                    func.display_image(res.crossroadx3_left)
                case 2:
                    func.display_image(res.crossroadx3_right)
        if random.randint(1,8) == 1:
            Resources.playsound.play_horror_sfx()


    
        