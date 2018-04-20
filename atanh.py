import math

def ATanh(param1,param2, param3):
    try:
        if param1==0:
            if param3 == False:
                param1=math.atanh(float(param2))
            elif param3==True:
                param1=math.atanh(float(param2))
        else:
            if param3 == False:
                param1=math.atanh(float(param1))
            elif param3== True:
                param1=math.atanh(float(param1))
    except:
        pass
    return param1, ''
