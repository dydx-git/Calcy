def Subtract(param1, param2):
    try:
        if param1 == None:
            param1 = 0
            param1-=float(param2)
            param1*=-1
        else:
            param1-=float(param2)
    except:
        pass
    return param1, ''
