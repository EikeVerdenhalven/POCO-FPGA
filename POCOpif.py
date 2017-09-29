#!/usr/bin/env python
from __future__ import division
import sys
import ctypes
import pifglobs
import struct
from asciimatics.screen import Screen
from time import sleep

# ------------------------------------------------------------------------------
# print FPGA device identifier
# ------------------------------------------------------------------------------


def showDeviceID(handle):

    dw = ctypes.c_ulong(0xdeadbeef)
    res = pifglobs.pif.pifGetDeviceIdCode(handle, ctypes.byref(dw))
    if (res == 0):
        print("\nread ID code failed\n")
        return "failed"

    deviceID = dw.value
    print('XO2 Device ID: %08x' % deviceID),

    s = pifglobs.UNRECOGNIZED
    ok = (deviceID & 0xffff8fff) == (0x012ba043 & 0xffff8fff)
    model = (deviceID >> 12) & 7

    if model == 0:
        s = "XO2-256HC"
    elif model == 1:
        s = "XO2-640HC"
    elif model == 2:
        s = "XO2-1200HC"
    elif model == 3:
        s = "XO2-2000HC"
    elif model == 4:
        s = "XO2-4000HC"
    elif model == 5:
        s = "XO2-7000HC"
    else:
        s = pifglobs.UNRECOGNIZED
        ok = False

    if ok:
        print(" - device is an " + s)
    else:
        print(" - unrecognised ID!")

    return s

# ------------------------------------------------------------------------------
# send the start command, that resets the LED address counter
# ------------------------------------------------------------------------------


def sendCommand(handle):
    try:
        cmdLength = 1
        buff = ctypes.create_string_buffer(chr(0x8A), cmdLength)
        pifglobs.pif.pifAppWrite(handle, buff, cmdLength)
    except:
        print('FAILED: command byte send')

# ------------------------------------------------------------------------------
# read a single LED entry from FPGA
# ------------------------------------------------------------------------------


def readLED(handle):
    cmdLength = 4
    buff = ctypes.create_string_buffer(cmdLength)
    res = pifglobs.pif.pifAppRead(handle, buff, cmdLength)
    if res == 1:
        return struct.unpack_from("=HH", buff)
    else:
        return (0, 0)

# ------------------------------------------------------------------------------
# format a single LED data entry
# ------------------------------------------------------------------------------


def format_data(idx, data):
    t_off = data[0]
    t_on = data[1]
    total = t_off + t_on
    ratio = 0.0
    if total != 0:
        ratio = t_on / total
    format_string = "{0: >2}: {1: >5}/{2: >5}={3: >5.1F}%"
    return format_string.format(idx, t_on, t_off, ratio * 100.0)

# ------------------------------------------------------------------------------
# print LED data for a bus
# ------------------------------------------------------------------------------


def printLEDs(handle, screen):
    idx = 0
    for row in range(0, 37):
        colpos = 0

        c1 = format_data(idx, readLED(handle))
        screen.print_at(c1, colpos, int(row))
        colpos = colpos + len(c1) + 8
        idx = idx + 1

        c2 = format_data(idx, readLED(handle))
        screen.print_at(c2, colpos, int(row))
        colpos = colpos + len(c2) + 8
        idx = idx + 1

        c3 = format_data(idx, readLED(handle))
        screen.print_at(c3, colpos, int(row))
        idx = idx + 1

    screen.print_at(format_data(idx, readLED(handle)), 0, 37)


def read_LEDs_A(handle, screen):
    for i in range(1, 4000):
        sendCommand(handle)
        printLEDs(handle, screen)
        screen.refresh()
        sleep(0.075)

# ------------------------------------------------------------------------------
# read all LED data from FPGA
# ------------------------------------------------------------------------------


def get_LED_data(handle):
    sendCommand(handle)
    LEDList = []
    for I in range(1, 336):
        lednums = readLED(handle)
        t_off = lednums[0]
        t_on = lednums[1]
        total = t_off + t_on
        ratio = 0.0
        if total != 0:
            ratio = t_on / total
        LEDList.append(ratio)
    return LEDList

# ------------------------------------------------------------------------------
# trigger signal sampler for debug purposes
# ------------------------------------------------------------------------------


def trigger(handle):
    try:
        cmdLength = 1
        buff = ctypes.create_string_buffer(chr(0x8B), cmdLength)
        pifglobs.pif.pifAppWrite(handle, buff, cmdLength)
    except:
        print('FAILED: command byte send')


def prep_read(handle):
    try:
        cmdLength = 1
        buff = ctypes.create_string_buffer(chr(0x8C), cmdLength)
        pifglobs.pif.pifAppWrite(handle, buff, cmdLength)
    except:
        print('FAILED: command byte send')


def write_scope(handle):
    trigger(handle)
    prep_read(handle)
    try:
        for i in range(1, 2047):
            cmdLength = 1
            buff = ctypes.create_string_buffer(cmdLength)
            res = pifglobs.pif.pifAppRead(handle, buff, cmdLength)
            if res == 1:
                byte = struct.unpack_from("B", buff)[0]
                print("{0:08b}".format(byte))
    except:
        print('FAILED: reading 4 bytes')


def scope(handle, screen):
    for i in range(0, 10):
        write_scope(handle, screen)
        sleep(0.5)


def captureHandle(handle):
    return lambda s: read_LEDs_A(handle, s)


def main():
    handle = None
    try:
        pifglobs.pif = ctypes.CDLL("libpif.so")

        strBuf = create_string_buffer(1000)
        rv = pifglobs.pif.pifVersion(strBuf, sizeof(strBuf))
        print('Using pif library version: %s\n' % repr(strBuf.value))

        handle = ctypes.c_int(pifglobs.pif.pifInit())
        dev = showDeviceID(handle)

        if dev != pifglobs.UNRECOGNIZED:
            print('pif detected')
            pifglobs.handle = handle

#      test_reads(handle)
#      write_scope(handle)
#      Screen.wrapper(captureHandle(handle))
        for I in range(1, 100):
            ledlist = get_LED_data(handle)
            print('\n'.join('{}: {}'.format(*k) for k in enumerate(ledlist)))
            sleep(0.5)
    except AttributeError as attrerr:
        print("AttributeError {0}".format(attrerr))
    except TypeError as ter:
        print("TypeError {0}".format(ter))
    except NameError as err:
        print("NameError {0}".format(err))
    except:
        print("Exception caught ", sys.exc_info()[0])

    if handle:
        pifglobs.pif.pifClose(handle)


if __name__ == '__main__':
    main()
