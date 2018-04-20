#def Factorial(number):
#    ans = 1
#    for i in range(1,number+1):
#        ans=ans*i
#        return ans

import math
def Fact(param1,param2):
    try:
        if param1 == None:
            param1 = math.factorial(float(param2))
        else:
            param1 = math.factorial(float(param1))
    except:
        pass
    return param1, ''
            


    
