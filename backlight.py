#!/usr/bin/env python3

import sys
import os

BACKLIGHT_DIR = '/sys/class/backlight/intel_backlight'
BRIGHTNESS_PATH = os.path.join(BACKLIGHT_DIR, 'brightness')
MAX_BRIGHTNESS_PATH = os.path.join(BACKLIGHT_DIR, 'max_brightness')

brightness_incriment = 0.01

max_brightness = 0

with open(MAX_BRIGHTNESS_PATH, 'r') as max_brightness_file:
    max_brightness = int(max_brightness_file.read())

def get_brightness():
    with open(BRIGHTNESS_PATH, 'r') as brightness_file:
        return int(brightness_file.read())

def write_brightness(data: str):
    with open(BRIGHTNESS_PATH, 'wt') as brightness_file:
        brightness_file.write(data)

def adjust_brightness(percentage: float):
    goal_brightness = max(min(int(max_brightness * percentage), max_brightness), 0)

    write_brightness(str(goal_brightness))

def increase_brightness(incriment: int):
    brightness_percentage = ((get_brightness() / float(max_brightness)) * 100) + incriment

    set_brightness(brightness_percentage)

def set_brightness(percentage: int):
    adjust_brightness(percentage / 100.0)

if __name__ == '__main__':
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print('usage: backlight.py [increase|decrease|set] [brightness_input]')
        sys.exit(1)
    
    command = sys.argv[1]

    if command == 'get':
        print(f'{int(round(get_brightness() / float(max_brightness) * 100))}%')
    elif command == 'increase':
        increase_brightness(10)
    elif command == 'decrease':
        increase_brightness(-10)
    elif command == 'set':
        brightness_input = int(sys.argv[2])
        set_brightness(brightness_input)
    else:
        print('Invalid Option')
        print('usage: python script.py [increase|decrease|set] [brightness_input]')
        sys.exit(1)
