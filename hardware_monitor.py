import POCOstub
from asciimatics.screen import Screen
from time import sleep


def format_entry(index, ratio):
    return "{0: >2}: {1: >5.1F}%".format(index, ratio)


def print_led_data(screen, data):
    row = 0
    index = 0
    while index < 96:
        col = 0
        for colidx in range(0, 3):
            s = format_entry(index, data[index])
            index += 1
            screen.print_at(s, col, row)
            col += len(s) + 2
        row += 1


def update_repl(screen):
    for I in range(1, 100):
        data = POCOstub.get_LED_data()
        print_led_data(screen, data)
        screen.refresh()
        sleep(0.5)


Screen.wrapper(update_repl)
