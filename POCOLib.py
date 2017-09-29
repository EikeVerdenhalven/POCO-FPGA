import POCOpif


class POCOLib(object):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.__POCOHANDLE__ = POCOpif.initialize_pif()

    def deinit(self):
        if self.__POCOHANDLE__:
            POCOpif.deinit_pif(self.__POCOHANDLE__)
            self.__POCOHANDLE__ = None

    def get_Keybed_RGB_LED(self, index):
        data = POCOpif.get_LED_data(self.__POCOHANDLE__)
        if index > 0 and index < 32:
            return data[index], data[index + 1], data[index + 2]
        else:
            index += 112
            return data[index], data[index + 1], data[index + 2]
