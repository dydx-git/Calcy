import math

def Log(param1,param2):
    if param1 == None and float(param2)>0:
        param1=math.log10(float(param2))
    else:
        if param1>0:
            param1=math.log10(float(param1))
    return param1, ''
