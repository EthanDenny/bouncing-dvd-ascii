# Bouncing DVD logo
# Built to run in an 80x24 terminal (the default size)

import math
import time
import random

DVD = '⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡀⠀⢠⣿⣿⡿⠀⠀⠈⢹⣿⣿⡿⣿⣿⣇⠀⣠⣿⣿⠟⣽⣿⣿⠇⠀⠀⢹⣿⣿⣿⠀⢸⣿⣿⡇⠀⢀⣠⣾⣿⡿⠃⢹⣿⣿⣶⣿⡿⠋⢰⣿⣿⡿⠀⠀⣠⣼⣿⣿⠏⠀⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⢿⣿⣿⠏⠀⠀⢸⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣸⣟⣁⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⣿⣿⣻⡟⣻⣿⢻⣿⡟⣛⢻⣿⡟⣛⣿⡿⣛⣛⢻⣿⣿⣶⣦⣄⡀⠀⠉⠛⠻⠿⠿⠿⠷⣼⣿⣿⣼⣿⣧⣭⣼⣿⣧⣭⣿⣿⣬⡭⠾⠿⠿⠿⠛⠉⠀⠀'

COLUMNS = 30
ROWS = 7

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24

logo_offset_x = 0
logo_offset_y = 0

angle = 45

while True:
    time.sleep(0.1)

    out = ''

    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            rounded_off_x = round(logo_offset_x)
            rounded_off_y = round(logo_offset_y)
            if rounded_off_x <= x < rounded_off_x + COLUMNS and rounded_off_y <= y < rounded_off_y + ROWS:
                out += DVD[x - rounded_off_x + (y - rounded_off_y) * COLUMNS]
            else:
                out += '⠀'
        out += '\n'

    print('\033[2J\033[H' + out)

    logo_offset_x += math.cos(angle) * 1.5 # Adjust for font size
    logo_offset_y += math.sin(angle)

    if logo_offset_x < 0 or SCREEN_WIDTH - COLUMNS <= logo_offset_x:
        logo_offset_x = max(0, min(logo_offset_x, SCREEN_WIDTH - COLUMNS))
        angle = random.randrange(360)

    if logo_offset_y < 0 or SCREEN_HEIGHT - ROWS <= logo_offset_y:
        logo_offset_y = max(0, min(logo_offset_y, SCREEN_HEIGHT - ROWS))
        angle = random.randrange(360)
