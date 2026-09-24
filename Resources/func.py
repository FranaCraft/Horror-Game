import time, curses, keyboard
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


def display_image(image):
    def draw(screen):
        screen.clear()

        height, width = screen.getmaxyx()
        image_height = len(image)
        image_width = max(len(line) for line in image)

        start_y = (height - image_height) // 2
        start_x = (width - image_width) // 2

        for index, line in enumerate(image):
            y = start_y + index

            if 0 <= y < height:
                x = max(0, start_x)
                line_start = max(0, -start_x)
                visible_line = line[line_start:]
                visible_line = visible_line[:width - x]

                if visible_line:
                    screen.addstr(y, x, visible_line)

        screen.refresh()
        screen.getch()

    curses.wrapper(draw)

def key(num:int):
    if num == 4:
        while True:
            if keyboard.is_pressed("j"):
                return 1
    elif num == 3:
        pass
    else:
        raise ValueError
    
    
        
    
    
    
    
    










    
    