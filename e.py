import math
def E(param1,param2):
     try:
          if param1==None and param2=='':
               param1=math.exp(1)
          elif param1 == None:
               param1=math.exp(int(param2))
          else:
               param1=math.exp(int(param1))
          print(param1)
           
     except:
          pass
     return param1, ''
