import time
fr = ""

def que(numb=int,choice=list):
    fr = ""
    for i in range(numb):
        fr = (f"{fr}\n{i + 1}) {choice[i]}")
    print(fr)
    urchoice = input(": ")
    if not urchoice == int:
        print("Write a valid number!")
    if urchoice > numb:
        print(f"Write number between 1-{numb}")
    return 
    
    