

def get_LED_data():
    retval = []
    for chain in range(0, 3):
        for I in range(0, 112):
            retval.append(I * (1.0 / 112.0) * 100.0)
    return retval
