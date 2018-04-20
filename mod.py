def Mod(param1, param2):
    if param1 == None:
        param1=0
        param1+=1
        param1=float(param2)%param1
        param1+=float(param2)
        print('mod answer is: ', param1)
    else:
        if param1>0:
            param1%=float(param2)
            print('2nd mod answer is: ', param1)

    return param1, ''
