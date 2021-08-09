import numpy, talib

def get_MA(all_closes):

    np_closes = numpy.array(all_closes)
    ALL_SHORT_MA = talib.MA(np_closes, timeperiod=100)
    #ALL_SHORT_MA = talib.MA(np_closes, timeperiod=20, matype=0)

    SHORT_MA = []

    for x in ALL_SHORT_MA[-20:]:
        SHORT_MA.append(x)

    return SHORT_MA