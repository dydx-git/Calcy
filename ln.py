import math

def Ln(param1,param2):
    if param1 == None:
        param1=math.log(float(param2))
    else:
        param1=math.log(float(param1))
    print("its being called")
    return param1, ''
