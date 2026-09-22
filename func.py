import time
fr = ""

def que(numb=int,choice=list,input=str):
    fr = ""
    for i in range(numb):
        fr = (f"{fr}\n{i + 1}) {choice[i]}")
    print(fr)
    urchoice = input(": ")
    while not urchoice == int or urchoice > numb:
        print(f"Write valid number between 1-{numb}")
        time.sleep(2)
        urchoice = input(f"{input}: ")
        
    return  urchoice
    
    