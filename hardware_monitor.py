import POCOstub
from asciimatics.screen import Screen
from time import sleep


def format_entry(index, ratio):
    return "{0: >2}: {1: >5.1F}%".format(index, ratio)


def print_rgb_led_data(screen, data, offset=0):
    row = 0
    index = offset
    col_offset = 0
    while index < len(data):
        prefix = "{0: >3}: ".format(index)
        screen.print_at(prefix, col_offset, row)
        col = col_offset + len(prefix) + 2
        for color_letter in ['R', 'G', 'B']:
            s = format_entry(color_letter, data[index])
            index += 1
            screen.print_at(s, col, row)
            col += len(s) + 2
        row += 1
        if row > screen.dimensions[0]:
            row = 0
            col_offset += 46


def update_repl(screen):
    for I in range(1, 100):
        data = POCOstub.get_LED_data()
        print_rgb_led_data(screen, data, 0)
        screen.refresh()
        sleep(0.5)

#print(len(POCOstub.get_LED_data()))
Screen.wrapper(update_repl)
