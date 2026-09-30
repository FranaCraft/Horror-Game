
import Resources.func as func, Resources.res as res, random, Resources.playsound, time
lines = ["i think i hear a something... ou sh*t!", "i think i hear water... and then you see the big wave it flushes you of water is risi...n..g.......", "i think i hear something moving", "wait i hear something..."]
intro = "You are Traped in Drainage System and maybe..."
intro2 = "...there is something with you."
intro3 = "and you need to get out of here, but quick! because water level is rising!"
outro = "hey wait i see light!"
outro2 = "finally light. last ladder and iam out"
def end():
    Resources.playsound.stop_horror_background_music()
    print("Thanks for playing this game, hope you enjoyed it \n Credits: \n Game made by: FranaCraft \n Story by: Bára Votrubová, Ema podzemská, FranaCraft  \n Music: @tanweraman,@cooljune452 \n SFX: @freesound_community")
    time.sleep(10)
    quit()
print(intro)
time.sleep(4)
print(intro2)
time.sleep(4)
print(intro3)
time.sleep(5)
until_next_thng = 3 + random.randint(-2,5)
lineslengh = len(lines)
for level in range(4):
    for ch_counter in range(until_next_thng):
        until_next_thng = 3 + random.randint(-2,5)
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
    line = random.randint(0, len(lines) - 1)
    if random.randint(1, 5) == 2:
        print(lines[random.randint(0,1)])
        time.sleep(5)
        end()
    else:
        print(lines[random.randint(2,3)])
        time.sleep(5)
    

print(outro)
time.sleep(4)
print(outro2)
time.sleep(4)
print("you are out of the drainage system and you are safe for now")
time.sleep(4)
end()
