import math

def Sin(param1,param2, param3):
    try:
        if param1==None or param2 != '':
            if param3 == False:
                param1=math.sin(float(param2))
            else:
                param1=math.sin(math.radians(float(param2)))
        else:
            if param3 == False:
                param1=math.sin(float(param1))
            else:
                param1=math.sin(math.radians(float(param1)))
    except:
        pass
    return param1, ''

