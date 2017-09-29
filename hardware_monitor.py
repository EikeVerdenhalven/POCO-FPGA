import POCOpif
from asciimatics.screen import Screen
from time import sleep


def format_entry(index, ratio):
    return "{0: >2}: {1: >5.1F}%".format(index, ratio)


def print_rgb_led_data(screen, data, offset, size, initial_row=0, initial_col=0):
    row = initial_row
    index = offset
    col_offset = initial_col
    while index < offset + size:
        prefix = "{0: >3}: ".format(index)
        screen.print_at(prefix, col_offset, row)
        col = col_offset + len(prefix) + 2
        for color_letter in ['G', 'R', 'B']:
            s = format_entry(color_letter, data[index])
            index += 1
            screen.print_at(s, col, row)
            col += len(s) + 2
        row += 1
        if row > screen.dimensions[0]:
            row = 0
            col_offset += 44
    return row, col_offset


def update_repl(screen):
    handle = POCOpif.initialize_pif()
    for I in range(1, 100):
        data = POCOpif.get_LED_data(handle)
        last_position = print_rgb_led_data(screen, data, 0, 96)
        last_position = print_rgb_led_data(screen, data, 112, 96, last_position[0], last_position[1])
        screen.refresh()
        sleep(0.5)
    POCOpif.deinit_pif(handle)

def test_hw():
    handle = POCOpif.initialize_pif()
    data = POCOpif.get_LED_data(handle)
    print(len(data))
    POCOpif.deinit_pif(handle)

#test_hw()
#print(len(POCOstub.get_LED_data()))
Screen.wrapper(update_repl)
