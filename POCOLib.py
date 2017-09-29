import POCOpif


class POCOLib:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.__POCOHANDLE__ = POCOpif.initialize_pif()

    def _init_POCOhandle():
        global POCOhandle
        POCOhandle = POCOpif.initialize_pif()

    def deinit():
        global POCOhandle
        if POCOhandle:
            POCOpif.deinit_pif(POCOhandle)

    def get_Keybed_RGB_LED(index):
        data = POCOpif.get_LED_data(POCOhandle)
        if index > 0 and index < 32:
            return data[index], data[index + 1], data[index + 2]
        else:
            index += 112
            return data[index], data[index + 1], data[index + 2]
