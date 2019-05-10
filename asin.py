import math

def ASin(param1,param2,param3):
    try:
        if param1==None or param2!='':
            if param3 == False:
                param1=math.asin(float(param2))
            elif param3==True:
                param1=math.asin(float(param2))
                param1=math.degrees(param1)
        else:
            if param3 != True:
                param1=math.asin(float(param1))
            elif param3==True:
                param1=math.asin(float(param1))
                param1=math.degrees(param1)
    except:
        pass
    return param1, ''
