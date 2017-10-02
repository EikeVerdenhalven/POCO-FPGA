import subprocess
from time import sleep
from os import devnull


def _run_HID_tool(args):
    __HIDTOOL_EXE = "./NIHIDTool"
    cmd = [__HIDTOOL_EXE]
    FNULL = open(devnull, 'w')
    subprocess.call(cmd + args, stdout=FNULL, stderr=subprocess.STDOUT)


def _set_HID_mode():
    _run_HID_tool(["-w", "0xA0", "0x00", "0x00"])


def _format_char(x):
    return "0x{:0>2X}".format(x)


def _colors_to_arg_string(colors):
    stringed = [
        (_format_char(x[0]), _format_char(x[1]), _format_char(x[2]))
        for i, x in enumerate(colors)]
    colargs = ["-w", "0x82"]
    for x in stringed:
        for c in x:
            colargs.append(c)
    return colargs


def set_RGB_colors(colors):
    _run_HID_tool(_colors_to_arg_string(colors))


def fill_RGB_color(color, count):
    return [color for i in range(0, count)]


def set_single_Key_RGB(key, r, g, b, totalcount):
    cols = fill_RGB_color((0, 0, 0), totalcount)
    cols[key] = (r, g, b)
    set_RGB_colors(cols)
