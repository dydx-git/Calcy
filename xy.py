import math

def Xy(param1,param2):
    try:
        if param1==None:
            param1=1
            param1= math.pow(int(param2),param1)
        else:
            param1= math.pow(param1,int(param2))
    except:
        pass
    return param1, ''

