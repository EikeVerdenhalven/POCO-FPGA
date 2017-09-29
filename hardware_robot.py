#import POCOpif
import POCOstub


def get_LED_state(index):
    ledlist = POCOstub.get_LED_data()
    return ledlist[index]


print get_LED_state(1)
