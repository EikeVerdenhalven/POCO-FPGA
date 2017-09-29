import POCOpif

POCOhandle = None


def init_POCOhandle():
    global POCOhandle
    POCOhandle = POCOpif.initialize_pif()


def deinit_POCOhandle():
    global POCOhandle
    if POCOhandle:
        POCOpif.deinit_pif(POCOhandle)


def get_Keybed_RGB_LED(index):
    data = POCOpif.get_LED_data()
    if index > 0 and index < 32:
        return data[index], data[index + 1], data[index + 2]
    else:
        index += 112
        return data[index], data[index + 1], data[index + 2]
