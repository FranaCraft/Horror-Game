import time, curses
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


def _draw_image(screen, image):
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


def display_image(image, delay=2):
    def draw(screen):
        _draw_image(screen, image)
        curses.napms(max(0, int(delay * 1000)))

    curses.wrapper(draw)

def key(num:int, image):
    options = {4: {"j": 1, "k": 2, "l": 3}, 3: {"j": 1, "l": 2}}
    if num not in options:
        raise ValueError("A crossroads must have either 3 or 4 paths")

    choices = options[num]

    def read_choice(screen):
        _draw_image(screen, image)
        while True:
            pressed = screen.getch()
            try:
                key_char = chr(pressed).lower()
            except ValueError:
                continue
            if key_char in choices:
                return choices[key_char]

    return curses.wrapper(read_choice)
