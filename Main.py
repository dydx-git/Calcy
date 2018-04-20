#<--------------------------------------------------------------------------------------IMPORTS------------------------------------------------------------------------>
from tkinter import *
import add, subtract, multiply, divide, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, log, ln, x2, xy, e, fact, x3, sqrt, cubert, mod

#<---------------------------------------------------------------------------------------GLOBALS------------------------------------------------------------------------>
root= Tk()
root.title('Calcy')
num1=StringVar()
ans = None
common = ''
condition = ''
isOpAllowed = False
listOfNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
isDegreeOn = True
mem = None
num1.set("Start Calculation")
isExtraOff = False
finalans = None

#<---------------------------------------------------------------------------------------ENTRY MANAGEMENT---------------------------------------------------------------->
def Clear():
    global ans, common, isOpAllowed, condition
    ans = None
    condition = ''
    common = ''
    isOpAllowed = False
    num1.set('0')
    history = ''

def Backspace(event):
    global common, ans
    if common=='':
        pass
    else:
        common = str(common)[:-1]
        num1.set(common)

#<---------------------------------------------------------------------------------------SETTERS------------------------------------------------------------------------->
def SetAns():
    global ans, finalans
    print('this is ans:', ans)
    print(common)
    try:
        i = str(ans).index('.')
        tempans = str(ans)[-1: i: -1]
        print('this is ans:', ans)
        if '0.' in str(ans):
            num1.set(round(ans,12))
        else:
            for digit in tempans:
                if digit in listOfNumbers:
                    num1.set(round(ans,12))
                elif tempans == '0':
                    finalans = str(ans)[:i]
                    num1.set(finalans)
                else:
                    finalans = str(ans)[:i]
                    num1.set(finalans)
    except:
        pass


def SetAdd(event):
    global condition
    if condition == '':
        GetAdd()
    else:
        decider[condition]()
    condition = '+'
    SetAns()
    global isOpAllowed
    isOpAllowed = True

def SetSubtract(event):
    global condition, isOpAllowed
    if condition == '':
        GetSubtract()
    else:
        decider[condition]()
    condition = '-'
    SetAns()
    isOpAllowed = True


def SetMultiply(event):
    global condition, isOpAllowed
    if condition == '':
        GetMultiply()
    else:
        decider[condition]()
    condition = '*'
    SetAns()
    isOpAllowed = True

def SetDivide(event):
    global condition, isOpAllowed
    if condition == '':
        GetDivide()
    else:
        decider[condition]()
    condition = '/'
    SetAns()
    isOpAllowed = True

def SetMod():
    global condition, isOpAllowed
    if condition == '':
        GetMod()
    else:
        decider[condition]()
    condition = 'mod'
    SetAns()
    isOpAllowed = True

def SetSin():
    GetSin()
    SetAns()

def SetCos():
    GetCos()
    SetAns()

def SetTan():
    GetTan()
    SetAns()

def SetASin():
    GetASin()
    SetAns()

def SetACos():
    GetACos()
    SetAns()

def SetATan():
    GetATan()
    SetAns()

def SetSinh():
    GetSinh()
    SetAns()

def SetCosh():
    GetCosh()
    SetAns()

def SetTanh():
    GetTanh()
    SetAns()

def SetASinh():
    GetASinh()
    SetAns()

def SetACosh():
    GetACosh()
    SetAns()

def SetATanh():
    GetATanh()
    SetAns()

def SetLog(event):
    GetLog()
    SetAns()

def SetLn(event):
    GetLn()
    SetAns()

def SetX2(event):
    GetX2()
    SetAns()

def SetX3():
    GetX3()
    SetAns()

def SetXy(event):
    global condition, isOpAllowed
    if condition == '':
        GetXy()
    else:
        decider[condition]()
    condition = 'xy'
    SetAns()
    isOpAllowed = True
    SetAns()

def SetE(event):
    GetE()
    SetAns()

def SetSqrt():
    GetSqrt()
    SetAns()

def SetCubert():
    GetCubert()
    SetAns()

def SetFact(event):
    GetFact()
    num1.set(ans)

def SetEquals(event):
    global condition, isOpAllowed, ans
    decider[condition]()
    SetAns()
    condition = ''
    ans = None
    common = ''
#<---------------------------------------------------------------------------------------GETTERS----------------------------------------------------------------------->
def GetAdd():
    global ans, common
    ans, common = add.Add(ans, common)

def GetSubtract():
    global ans, common
    ans, common = subtract.Subtract(ans, common)

def GetMultiply():
    global ans, common
    ans, common = multiply.Multiply(ans, common)

def GetDivide():
    global ans, common
    ans, common = divide.Divide(ans, common)

def GetSin():
    global ans, common, isDegreeOn
    ans, common = sin.Sin(ans,common, isDegreeOn)

def GetCos():
    global ans, common, isDegreeOn
    ans, common = cos.Cos(ans,common, isDegreeOn)

def GetTan():
    global ans, common, isDegreeOn
    ans, common = tan.Tan(ans, common, isDegreeOn)

def GetASin():
    global ans, common, isDegreeOn
    ans, common = asin.ASin(ans,common, isDegreeOn)

def GetACos():
    global ans, common, isDegreeOn
    ans, common = acos.ACos(ans,common, isDegreeOn)

def GetATan():
    global ans, common, isDegreeOn
    ans, common = atan.ATan(ans,common, isDegreeOn)

def GetSinh():
    global ans, common, isDegreeOn
    ans, common = sinh.Sinh(ans,common, isDegreeOn)

def GetCosh():
    global ans, common, isDegreeOn
    ans, common = cosh.Cosh(ans,common, isDegreeOn)

def GetTanh():
    global ans, common, isDegreeOn
    ans, common = tanh.Tanh(ans,common, isDegreeOn)

def GetASinh():
    global ans, common, isDegreeOn
    ans, common = asinh.ASinh(ans,common, isDegreeOn)

def GetACosh():
    global ans, common, isDegreeOn
    ans, common = acosh.ACosh(ans,common, isDegreeOn)

def GetATanh():
    global ans, common, isDegreeOn
    ans, common = atanh.ATanh(ans,common, isDegreeOn)

def GetLog():
    global ans, common
    ans, common = log.Log(ans, common)

def GetLn():
    global ans, common
    ans, common = ln.Ln(ans, common)

def GetX2():
    global ans, common
    ans, common = x2.X2(ans, common)

def GetX3():
    global ans, common
    ans, common = x3.X3(ans, common)

def GetXy():
    global ans, common
    ans, common = xy.Xy(ans, common)

def GetE():
    global ans, common
    ans, common = e.E(ans, common)

def GetSqrt():
    global ans, common
    ans, common = sqrt.Sqrt(ans, common)

def GetCubert():
    global ans, common
    ans, common = cubert.Cubert(ans, common)

def GetFact():
    global ans, common
    ans, common = fact.Fact(ans, common)

def GetMod():
    global ans, common
    ans, common = mod.Mod(ans, common)
#<--------------------------------------------------------------------------------------MEMORY MANAGER----------------------------------------------------------------->

def MC():
    global mem
    mem = None

def MR():
    global mem, common
    if mem != None:
        common = mem
    else:
        pass
        print('this is MR:', common)
    num1.set(common)

def MS():
    global mem, common, ans
    if common != '':
        mem = int(common)
    else:
        print(ans)
        mem = str(ans)

#<------------------------------------------------------------------------------------DEGREE/RADIAN------------------------------------------------------------------- >
def DegRad():
    global isDegreeOn
    if isDegreeOn == False:
        isDegreeOn = True
        degRadButton.config(image=imgDeg)
    elif isDegreeOn == True:
        isDegreeOn = False
        degRadButton.config(image=imgRad)

#<----------------------------------------------------------------------------------EXTRAS MANAGER---------------------------------------------------------------------->
def ActivateExtra():
    global isExtraOff
    if isExtraOff == False:
        asinButton.grid(row=3,column=0)
        acosButton.grid(row=4,column=0)
        atanButton.grid(row=5,column=0)
        asinhButton.grid(row=7, column=0)
        acoshButton.grid(row=7, column=1)
        atanhButton.grid(row=7, column=2)
        lnButton.grid(row=7, column=3)
        x3Button.grid(row=2, column = 0)
        cubertButton.grid(row=2, column=4)
        modButton.grid(row=8, column=0)
        hisLabel.grid(row=0, column=2, columnspan=3, pady=(60,0))
        xtraButton.config(image=imgXtra2)
        isExtraOff = True
    else:
        acosButton.grid_forget()
        asinButton.grid_forget()
        atanButton.grid_forget()
        acoshButton.grid_forget()
        asinhButton.grid_forget()
        atanhButton.grid_forget()
        lnButton.grid_forget()
        x3Button.grid_forget()
        cubertButton.grid_forget()
        modButton.grid_forget()
        hisLabel.place(x=10,y=10)
        xtraButton.config(image=imgXtra1)
        isExtraOff = False

#<---------------------------------------------------------------------------------------ENTRY------------------------------------------------------------------------->

txtDisplay = Entry(root, textvariable = num1, width=17,justify="right", fg='white', borderwidth=0);
txtDisplay.config(readonlybackground='#0b486b', font = ("Segoe UI", 26))
txtDisplay.focus();
txtDisplay.config(state='readonly')
txtDisplay.grid(columnspan=7,row=0,ipady=6, pady=(0,24))

#<--------------------------------------------------------------------------------------DECORATING BUTTONS------------------------------------------------------------->
img1 = PhotoImage(file="assets/nb1.png")
img2 = PhotoImage(file="assets/nb2.png")
img3 = PhotoImage(file="assets/nb3.png")
img4 = PhotoImage(file="assets/nb4.png")
img5 = PhotoImage(file="assets/nb5.png")
img6 = PhotoImage(file="assets/nb6.png")
img7 = PhotoImage(file="assets/nb7.png")
img8 = PhotoImage(file="assets/nb8.png")
img9 = PhotoImage(file="assets/nb9.png")
imgPlus = PhotoImage(file="assets/+.png")
imgMinus = PhotoImage(file="assets/-.png")
imgMultiply = PhotoImage(file="assets/x.png")
imgDivide = PhotoImage(file="assets/dvd.png")
imgMC = PhotoImage(file='assets/MC.png')
imgMR = PhotoImage(file='assets/MR.png')
imgMS = PhotoImage(file='assets/MS.png')
imgBKSPC = PhotoImage(file='assets/backspace.png')
imgX2 = PhotoImage(file='assets/x2.png')
imgX3 = PhotoImage(file='assets/x3.png')
imgxy = PhotoImage(file='assets/xy.png')
imgSin = PhotoImage(file='assets/sin.png')
imgCos = PhotoImage(file='assets/cos.png')
imgTan = PhotoImage(file='assets/tan.png')
imgAsin = PhotoImage(file='assets/asin.png')
imgAcos = PhotoImage(file='assets/acos.png')
imgAtan = PhotoImage(file='assets/atan.png')
imgAsinh = PhotoImage(file='assets/asinh.png')
imgAcosh = PhotoImage(file='assets/acosh.png')
imgAtanh = PhotoImage(file='assets/atanh.png')
imgSinh = PhotoImage(file='assets/sinh.png')
imgCosh = PhotoImage(file='assets/cosh.png')
imgTanh = PhotoImage(file='assets/tanh.png')
imgDec = PhotoImage(file='assets/dec.png')
img0 = PhotoImage(file='assets/nb0.png')
imgDeg = PhotoImage(file='assets/deg.png')
imgRad = PhotoImage(file='assets/rad.png')
imgLog = PhotoImage(file='assets/log.png')
imgLn = PhotoImage(file='assets/ln.png')
imgE = PhotoImage(file='assets/e.png')
imgPi = PhotoImage(file='assets/pi.png')
imgC = PhotoImage(file='assets/c.png')
imgFact = PhotoImage(file='assets/fact.png')
imgSqrt = PhotoImage(file='assets/sqrt.png')
imgCubert = PhotoImage(file='assets/cubert.png')
imgPM = PhotoImage(file='assets/PM.png')
imgEquals = PhotoImage(file='assets/equals.png')
imgXtra1 = PhotoImage(file='assets/blue.png')
imgXtra2 = PhotoImage(file='assets/red.png')
imgdydx = PhotoImage(file='assets/dydx.png')
imgMod = PhotoImage(file='assets/mod.png')
dydxLabel = Label(root, image=imgdydx, bg='#232323')
dydxLabel.grid(row=8, column=2, columnspan=2)

#<---------------------------------------------------------------------------------------DEFINING BUTTONS------------------------------------------------------------------------->
oneButton = Button(root, height = '32', width='32', borderwidth=0, image=img1, bg='#232323', highlightthickness=0,command = lambda: clck('', 1))
twoButton = Button(root, height = '32', width='32', borderwidth=0, image=img2, bg='#232323', highlightthickness=0,command = lambda: clck('', 2))
threeButton = Button(root, height = '32', width='32', borderwidth=0, image=img3, bg='#232323', highlightthickness=0,command = lambda: clck('', 3))
fourButton = Button(root, height = '32', width='32', borderwidth=0, image=img4, bg='#232323', highlightthickness=0,command = lambda: clck('', 4))
sevenButton = Button(root, height = '32', width='32', borderwidth=0, image=img7, bg='#232323', highlightthickness=0,command = lambda: clck('', 7))
eightButton = Button(root, height = '32', width='32', borderwidth=0, image=img8, bg='#232323', highlightthickness=0,command = lambda: clck('', 8))
nineButton = Button(root, height = '32', width='32', borderwidth=0, image=img9, bg='#232323', highlightthickness=0,command = lambda: clck('', 9))
fiveButton = Button(root, height = '32', width='32', borderwidth=0, image=img5, bg='#232323', highlightthickness=0,command = lambda: clck('', 5))
sixButton = Button(root, height = '32', width='32', borderwidth=0, image=img6, bg='#232323', highlightthickness=0,command = lambda: clck('', 6))
zeroButton = Button(root, height = '32', width='32', borderwidth=0, image=img0, bg='#232323', highlightthickness=0,command = lambda: clck('', 0))
clearButton = Button(root, height = '46', width='46', borderwidth=0, image=imgC, bg='#232323', highlightthickness=0,command=Clear)
addButton = Button(root, text="+", height = '32', width='32',borderwidth=0,  image=imgPlus, bg='#232323')
subButton = Button(root, text="-", height = '32', width='32',borderwidth=0,  image=imgMinus, bg='#232323')
mcButton = Button(root, text='MC',height = '46', width='67', borderwidth=0, image=imgMC, bg='#232323', highlightthickness=0, command=MC);
mrButton = Button(root, text='MR', height = '46', width='67', borderwidth=0, image=imgMR, bg='#232323', highlightthickness=0, command=MR);
msButton = Button(root, text='M+', height = '46', width='67',borderwidth=0, image=imgMS, bg='#232323', highlightthickness=0, command=MS);
multiplyButton = Button(root, text="*",height = '46', width='46' ,borderwidth=0,  image=imgMultiply, bg='#232323')
divideButton = Button(root, text="/",height = '46', width='46',borderwidth=0,  image=imgDivide, bg='#232323')
sinButton = Button(root, text='sin', height = '36', width='36',borderwidth=0, image=imgSin, bg='#232323', highlightthickness=0, command=SetSin);
cosButton = Button(root, text='cos', height = '36', width='36',borderwidth=0, image=imgCos, bg='#232323', highlightthickness=0, command=SetCos);
tanButton = Button(root, text='tan', height = '36', width='36',borderwidth=0, image=imgTan, bg='#232323', highlightthickness=0, command=SetTan);
asinButton = Button(root, text='asin', height = '36', width='36',borderwidth=0, image=imgAsin, bg='#232323', highlightthickness=0, command=SetASin);
decButton = Button(root, text='.', height = '36', width='36',borderwidth=0, image=imgDec, bg='#232323', highlightthickness=0, command =lambda: clck('', '.'))
degRadButton = Button(root, text='deg', borderwidth=0, bg='#232323', highlightthickness=0, command=DegRad, image=imgDeg)
xtraButton = Button(root,borderwidth=0, bg='#232323', highlightthickness=0, command=ActivateExtra, image=imgXtra1);
acosButton = Button(root, text='acos', height = '36', width='36',borderwidth=0, image=imgAcos, bg='#232323', highlightthickness=0, command=SetACos);
atanButton = Button(root, text='atan', height = '36', width='36',borderwidth=0, image=imgAtan, bg='#232323', highlightthickness=0, command=SetATan);
sinhButton = Button(root, text='sinh', height = '36', width='36',borderwidth=0, image=imgSinh, bg='#232323', highlightthickness=0, command=SetSinh);
coshButton = Button(root, text='cosh', height = '36', width='36',borderwidth=0, image=imgCosh, bg='#232323', highlightthickness=0, command=SetCosh);
tanhButton = Button(root, text='tanh', height = '36', width='36',borderwidth=0, image=imgTanh, bg='#232323', highlightthickness=0, command=SetTanh);
asinhButton = Button(root, text='asinh', height = '36', width='36',borderwidth=0, image=imgAsinh, bg='#232323', highlightthickness=0, command=SetASinh);
acoshButton = Button(root, text='acosh', height = '36', width='36',borderwidth=0, image=imgAcosh, bg='#232323', highlightthickness=0, command=SetACosh);
atanhButton = Button(root, text='atanh', height = '36', width='36',borderwidth=0, image=imgAtanh, bg='#232323', highlightthickness=0, command=SetATanh);
logButton = Button(root, text='log', height = '36', width='36',borderwidth=0, image=imgLog, bg='#232323', highlightthickness=0);
lnButton = Button(root, text='log', height = '36', width='36',borderwidth=0, image=imgLn, bg='#232323', highlightthickness=0);
backspaceButton = Button(root, width = '46', height = '46', image = imgBKSPC, bg = '#232323',borderwidth=0, highlightthickness=0)
x2Button = Button(root, width = '27', height = '29', image = imgX2, bg = '#232323',borderwidth=0, highlightthickness=0)
x3Button = Button(root, width = '27', height = '29', image = imgX3, bg = '#232323',borderwidth=0, highlightthickness=0, command=SetX3)
xyButton = Button(root, width = '27', height = '29', image = imgxy, bg = '#232323',borderwidth=0, highlightthickness=0)
eButton = Button(root, width = '27', height = '29', image = imgE, bg = '#232323',borderwidth=0, highlightthickness=0)
piButton = Button(root, width = '27', height = '29', image = imgPi, bg = '#232323',borderwidth=0, highlightthickness=0, command= lambda: clck('', 3.14159265358))
factButton = Button(root, width = '36', height = '36', image = imgFact, bg = '#232323',borderwidth=0, highlightthickness=0)
sqrtButton = Button(root, width = '36', height = '36', image = imgSqrt, bg = '#232323',borderwidth=0, highlightthickness=0, command=SetSqrt)
cubertButton = Button(root, width = '36', height = '36', image = imgCubert, bg = '#232323',borderwidth=0, highlightthickness=0, command=SetCubert)
equalsButton = Button(root, width = '36', height = '72', image = imgEquals, bg = '#232323',borderwidth=0, highlightthickness=0)
pmButton =  Button(root, width = '36', height = '36', image = imgPM, bg = '#232323',borderwidth=0, highlightthickness=0, command= lambda: clck('', '-'))
modButton = Button(root, width = '36', height = '36', image = imgMod, bg = '#232323',borderwidth=0, highlightthickness=0, command= SetMod)

#<---------------------------------------------------------------------------------------BUTTON PLACEMENTS-------------------------------------------------------------------->
mcButton.grid(row = 1, column = 0)
mrButton.grid(row = 1, column = 1)
msButton.grid(row = 1, column = 2)
clearButton.grid(row = 1, column = 3)
backspaceButton.grid(row=1, column = 4)
x2Button.grid(row=2, column = 0, ipady=12)
eButton.grid(row=2, column = 1, ipady=12)
xyButton.grid(row=2, column = 3, ipady=12)
sinButton.grid(row=3,column=0)
cosButton.grid(row=4,column=0)
tanButton.grid(row=5, column=0)
xtraButton.grid(row=6, column=0)
sevenButton.grid(row=3, column=1, ipady=8)
eightButton.grid(row=3, column=2)
nineButton.grid(row=3, column=3)
sixButton.grid(row=4, column=3, ipady=12)
fiveButton.grid(row=4, column=2)
fourButton.grid(row=4, column=1)
threeButton.grid(row=5, column=3, ipady=12)
twoButton.grid(row=5, column=2)
oneButton.grid(row=5, column=1)
decButton.grid(row=6, column=1)
zeroButton.grid(row=6, column=2)
degRadButton.grid(row=6, column=3)
sinhButton.grid(row=7, column=0)
coshButton.grid(row=7, column=1)
tanhButton.grid(row=7, column=2, ipady=12)
logButton.grid(row=7, column=3)
piButton.grid(row=2, column =2)
addButton.grid(row=3, column=4)
subButton.grid(row=4, column=4)
multiplyButton.grid(row=5, column=4)
divideButton.grid(row=6, column=4)
factButton.grid(row=8, column=0, ipady=8)
sqrtButton.grid(row=2, column=4)
pmButton.grid(row=8, column= 1)
equalsButton.grid(row=7, column=4, rowspan=2)

#<---------------------------------------------------------------------------------------CLICK/DECIDER------------------------------------------------------------------------>
def clck (event, number):
    global condition
    global isOpAllowed
    global ans
    print(isOpAllowed)
    print('Condition', condition)
    global common
    print(number)
    if '-' in common:
        print('this is common', common)
        common = list(common)
        common[0] = ''
        common = ''.join(common)
        num1.set(common)
    elif number == '-':
        common = str(number)+ common
        num1.set(common)
    else:
        common+= str(number)
        if common[0] == '.':
            common = '0' + common
            num1.set(common)
        elif common.count('.')>1 :
            num1.set('Not allowed')
            common = ''
        else:
            num1.set(common)

decider = {'+': GetAdd, '-': GetSubtract, '*':GetMultiply, '/':GetDivide, 'xy': GetXy, 'mod': GetMod}

#<---------------------------------------------------------------------------------------KEYBOARD BUTTON BINDERS------------------------------------------------------------------>
root.bind("1", lambda event, arg = 1 : clck(event, arg))
root.bind("2", lambda event, arg = 2 : clck(event, arg))
root.bind("3", lambda event, arg = 3 : clck(event, arg))
root.bind("4", lambda event, arg = 4 : clck(event, arg))
root.bind("5", lambda event, arg = 5 : clck(event, arg))
root.bind("6", lambda event, arg = 6 : clck(event, arg))
root.bind("7", lambda event, arg = 7 : clck(event, arg))
root.bind("8", lambda event, arg = 8 : clck(event, arg))
root.bind("9", lambda event, arg = 9 : clck(event, arg))
root.bind("0", lambda event, arg = 0 : clck(event, arg))
root.bind("<plus>", SetAdd)
root.bind("<minus>", SetSubtract)
root.bind("<asterisk>", SetMultiply)
root.bind("<slash>", SetDivide)
root.bind("<BackSpace>", Backspace)
root.bind("<period>",  lambda event, arg = '.' : clck(event, arg))
root.bind("<Return>", SetEquals)

#<--------------------------------------------------------------------------------------MOUSE BUTTON BINDERS------------------------------------------------------------------>
addButton.bind("<Button-1>", SetAdd)
subButton.bind("<Button-1>", SetSubtract)
multiplyButton.bind("<Button-1>", SetMultiply)
divideButton.bind("<Button-1>", SetDivide)
logButton.bind("<Button-1>", SetLog)
lnButton.bind("<Button-1>", SetLn)
x2Button.bind("<Button-1>", SetX2)
eButton.bind("<Button-1>", SetE)
backspaceButton.bind("<Button-1>", Backspace)
factButton.bind("<Button-1>", SetFact)
xyButton.bind("<Button-1>", SetXy)
equalsButton.bind("<Button-1>", SetEquals)
root.configure(background='#232323')
root.mainloop()
