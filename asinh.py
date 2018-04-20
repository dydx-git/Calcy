import math

def ASinh(param1,param2, param3):
    try:
        if param1==None or param2!='':
            if param3 == False:
                param1=math.asinh(float(param2))
            elif param3==True:
                param1=math.asinh(float(param2))
        else:
            if param3 == False:
                param1=math.asinh(float(param1))
            elif param3== True:
                param1=math.asinh(float(param1))
    except:
        pass
    return param1, ''
