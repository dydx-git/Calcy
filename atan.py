import math

def ATan(param1,param2,param3):
    try:
        if param1==None or param2!='':
            if param3 == False:
                param1=math.atan(float(param2))
            elif param3==True:
                param1=math.atan(float(param2))
                param1=math.degrees(param1)
        else:
            if param3 == False:
                param1=math.atan(float(param1))
            elif param3==True:
                param1=math.atan(float(param1))
                param1=math.degrees(param1)
    except:
        pass
    return param1, ''


#a=math.sin(45)
#print(a)
#b=math.asin(a)
#b=math.degrees(b)
#print(b)
