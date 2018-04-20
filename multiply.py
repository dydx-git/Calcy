def Multiply(param1, param2):
    try:
        if param1 == None:
            param1=0
            param1+=1
            param1*=float(param2)
        else:
            param1*=float(param2)
    except:
        pass
    return param1, ''
