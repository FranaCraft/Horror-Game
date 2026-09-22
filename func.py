import time
fr = ""

def que(numb=int,choice=list,inputt=str):
    fr = ""
    for i in range(numb):
        fr = (f"{fr}\n{i + 1}) {choice[i]}")
    print(fr)
    urchoice = int(input(f"{inputt}: "))
    while urchoice > numb:
        print(f"Write valid number between 1-{numb}")
        time.sleep(2)
        urchoice = int(input(f"{inputt}: "))
    return  urchoice
    
    