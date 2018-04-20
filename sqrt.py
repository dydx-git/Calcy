import math

def Sqrt(param1,param2):
    try:
        if param1 == None:
            param1= math.sqrt(float(param2))
        else:
            param1= math.sqrt(float(param1))
    except:
        pass
    return param1, ''
