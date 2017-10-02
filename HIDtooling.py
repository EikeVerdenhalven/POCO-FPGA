import subprocess


def run_HID_tool(args):
    __HIDTOOL_EXE = "./NIHIDTool"
    cmd = [__HIDTOOL_EXE]
    subprocess.call(cmd + args)


def set_HID_mode():
    run_HID_tool(["-w", "0xA0", "0x00", "0x00"])


def format_char(x):
    return "0x{:0>2X}".format(x)


def colors_to_arg_string(colors):
    stringed = [
        (format_char(x[0]), format_char(x[1]), format_char(x[2]))
        for i, x in enumerate(colors)]
    colargs = ["-w", "0x82"]
    for x in stringed:
        for c in x:
            colargs.append(c)
    return colargs


def set_RGB_colors(colors):
    set_HID_mode()
    run_HID_tool(colors_to_arg_string(colors))
