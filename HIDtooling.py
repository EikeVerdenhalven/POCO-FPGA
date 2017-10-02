import subprocess
from time import sleep
from os import devnull
from robot.api import logger


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


def set_key_RGB_percent(key, r, g, b, totalcount):
    set_single_Key_RGB(key, (r/100)*255, (g/100)*255, (b/100)*255, totalcount)


def _sqr(x):
    return x * x


def match_with_margin(a, b, error):
    return _sqr(a - b) < _sqr(error)


def match_RGB_with_error(act_rgb, exp_rgb, error):
    if not match_with_margin(act_rgb[0], exp_rgb[0], error):
        logger.error("R mismatch")
        raise
    if not match_with_margin(act_rgb[1], exp_rgb[1], error):
        logger.error("G mismatch")
        raise
    if not match_with_margin(act_rgb[2], exp_rgb[2], error):
        logger.error("B mismatch")
        raise
    pass
