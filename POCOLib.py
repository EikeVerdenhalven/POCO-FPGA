import POCOpif


class POCOLib(object):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.__POCOHANDLE__ = POCOpif.initialize_pif()
        if not self.__POCOHANDLE__:
            raise

    def deinit(self):
        if self.__POCOHANDLE__:
            POCOpif.deinit_pif(self.__POCOHANDLE__)
            self.__POCOHANDLE__ = None

    def get_Keybed_RGB_LED(self, index):
        data = POCOpif.get_LED_data(self.__POCOHANDLE__)
        if index >= 0 and index < 32:
            return data[3*index + 1], data[3*index], data[3*index + 2]
        else:
            return
            data[3*index - 112 + 1],
            data[3*index - 112],
            data[3*index + 2 - 112]
