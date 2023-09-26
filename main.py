import tkinter.filedialog
from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
import random
from mnk import *
from fur import *
from berh import *
from mnkw import *
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


matplotlib.use("TkAgg")

nameFile =''
distance=0

funl = []
funl1 = ""
fff=200
bbb=15
nameofcolomn = ""

numoftests = 5

l=0
progn = 0
d=0
results=0

root =Tk()

root.title("Prognapp")
root.geometry('1100x900')

root.resizable (width=False, height=False)



#l5 = ttk.Label(text="Warning: часть значений вне доверительного интервала")



def otrisovka():
    global results
    l = np.linspace(1, len(results), len(results))
    l1 = np.linspace(1,len(d),len(d))

    fig = Figure(figsize=(5, 5),dpi=100)

    fig, ax = plt.subplots()

    ax.plot(l,results, label = "Прогнозная функция")
    ax.plot(l1, d, ":", label = "Экспериментальные точки")
    ax.legend()


    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # Размещение холста в окне tkinter
    canvas.get_tk_widget().place(x=400,y=400)


    #plt.plot(l,results)
    #plt.title("График")
    #plt.plot(l1, d, ":")
    #plt.show()


    #k2 = max(np.max(d), np.max(results))
    #kk = np.linspace(0,k2, 10)
    #plt.yticks(kk, labels=kk)
    #plt.plot(l1, d,":")






def cl():
    global nameFile
    nameFile = inp.get()
    l1['text'] = "Путь к файлу "+nameFile

def cl1():
    global nameofcolomn
    nameofcolomn = inp1.get()
    l4['text'] = "Название столбца "+ nameofcolomn


def cl2():
    global l
    l = int(inp3.get())

    l2['text'] = "Длина данных "+ str(l)



def cl7():
    global progn

    progn = int(inp2.get())

    l3['text'] = "Длина прогнозирования "+ str(progn)


def clmnk():
    global l
    global  d
    global nameofcolomn

    if(l!=0):
        ddd = pd.read_csv(nameFile, nrows=l)
    else:
        ddd = pd.read_csv(nameFile)

    if(nameofcolomn==""):
        nameofcolomn = ddd.columns[0]

    d = ddd[nameofcolomn]
    global results
    results, flag = runmnk(d, progn, numoftests)
    if (flag == 0):
        window = Tk()
        window.title = "Warning"
        window.geometry('400x200')
        l5 = ttk.Label(window, text="Warning: часть значений вне доверительного интервала")

        l5.place(x=000, y=100)
    otrisovka()

def clberg():
    global  d
    global l
    global bbb
    global nameofcolomn
    if(l!=0):
        ddd = pd.read_csv(nameFile, nrows=l)
    else:
        ddd = pd.read_csv(nameFile)

    if(nameofcolomn==""):
        nameofcolomn = ddd.columns[0]

    d = ddd[nameofcolomn]
    global results
    results, flag2 =    runberg(d, progn, bbb)
    results = np.concatenate((d,results))
    if (flag2 == 0):
        window = Tk()
        window.title = "Warning"
        window.geometry('400x200')
        l5 = ttk.Label(window, text="Warning: часть значений вне доверительного интервала")

        l5.place(x=000, y=100)
    otrisovka()

def addsin():
    global funl
    funl.append(np.sin)
    global funl1
    funl1  = funl1 + "c*sin(x)+"
    l6['text'] = "Список функций: " + funl1[:-1]

    l6.place(x=0, y=700)

def addcos():
    global funl
    funl.append(np.cos)
    global funl1
    funl1  = funl1 + "c*cos(x)+"
    l6['text'] = "Список функций: " + funl1[:-1]

    l6.place(x=0, y=700)

def added():
    global funl
    funl.append(ed)
    global funl1
    funl1  = funl1 + "c+"
    l6['text'] = "Список функций: " + funl1[:-1]

    l6.place(x=0, y=700)

def addlog():

    global funl
    funl.append(log)
    global funl1
    funl1  = funl1 + "c*log(x)+"
    l6['text'] = "Список функций: " +funl1[:-1]

    l6.place(x=0, y=700)

def addsq():

    global funl
    funl.append(sq)
    global funl1
    funl1  = funl1 + "c*sqare+"
    l6['text'] = "Список функций: " +funl1[:-1]

    l6.place(x=0, y=700)

def addob():

    global funl
    funl.append(ob)
    global funl1
    funl1  = funl1 + "c/x+"
    l6['text'] = "Список функций: " + funl1[:-1]
    l6.place(x=0,y=700)


def addsqrt():

    global funl
    funl.append(xm2)
    global funl1
    funl1  = funl1 + "c*sqrt(x)+"
    l6['text'] = "Список функций: " + funl1[:-1]
    l6.place(x=0,y=700)

def addkub():

    global funl
    funl.append(kub)
    global funl1
    funl1  = funl1 + "c*x^3+"
    l6['text'] = "Список функций: " + funl1[:-1]
    l6.place(x=0,y=700)


def runmnkw():
    global funl
    global  d
    global l
    global nameofcolomn


    if(l!=0):
        ddd = pd.read_csv(nameFile, nrows=l)
    else:
        ddd = pd.read_csv(nameFile)

    if(nameofcolomn==""):
        nameofcolomn = ddd.columns[0]

    d = ddd[nameofcolomn]
    global results
    results, flag = runmnkw2(d,funl, progn)
    if (flag == 0):
        window = Tk()
        window.title = "Warning"
        window.geometry('400x200')
        l5 = ttk.Label(window, text="Warning: часть значений вне доверительного интервала")

        l5.place(x=000, y=100)

    otrisovka()

def ochistka():
    global funl
    global funl1
    funl = []
    funl1 = ""
    l6['text'] = "Список функций: " + funl1



def vibor():
    l6.place(x=0, y=700)



    btnadd1 = ttk.Button(text="sin", command=addsin)
    btnadd1.place(x=400,y =0)

    btnadd2 = ttk.Button(text="cos", command=addcos)
    btnadd2.place(x=400, y =40)

    btnadd3 = ttk.Button(text="x=const", command=added)
    btnadd3.place(x=400, y =80)

    btnadd4 = ttk.Button(text="log", command=addlog)
    btnadd4.place(x=400, y =120)

    btnadd5 = ttk.Button(text="x^2", command=addsq)
    btnadd5.place(x=400, y =160)

    btnadd8 = ttk.Button(text="sqrt", command=addsqrt)
    btnadd8.place(x=400, y=200)

    btnadd9 = ttk.Button(text="x^3", command=addkub)
    btnadd9.place(x=400, y=240)

    btnadd6 = ttk.Button(text="1/x", command=addob)
    btnadd6.place(x=400, y =280)

    btnrun = ttk.Button(text="Начать", command=runmnkw)
    btnrun.place(x=400, y =320)


    btnzab = ttk.Button(text="Очистить список", command=ochistka)
    btnzab.place(x=400, y =280)

def clfur2():

    global fff
    fff= int(inp4.get())

    clfur()

def cllmnk():
    global numoftests
    numoftests = int(inp10.get())

    clmnk()


def clberg2():

    global bbb
    bbb= int(inp5.get())

    clberg()

def openf():
    global nameFile
    nameFile = tkinter.filedialog.askopenfilename()
    l1['text'] = "Путь к файлу "+nameFile


def clfur():
    global  d
    global l
    global fff
    global nameofcolomn
    if(l!=0):
        ddd = pd.read_csv(nameFile, nrows=l)
    else:
        ddd = pd.read_csv(nameFile)

    if(nameofcolomn==""):
        nameofcolomn = ddd.columns[0]

    d = ddd[nameofcolomn]
    global results
    results, flag2 = runfur(d, progn,fff)
    if (flag2 == 0):
        window = Tk()
        window.title = "Warning"
        window.geometry('400x200')
        l5 = ttk.Label(window, text="Warning: часть значений вне доверительного интервала")

        l5.place(x=000, y=100)
    otrisovka()


def clvv():
    cl1()
    cl7()
    cl2()





btn = ttk.Button(text="Ввод имени файла", command=cl)
btn.place(x=0,y=0)


inp = Entry()
inp.place(x=200,y=0)

btn1 = ttk.Button( text="Ввод названия столбца", command=cl1)

btn1.place(x=0,y=40)


inp1 = Entry()
inp1.place(x=200,y=40)

btn2 = ttk.Button(text="Ввод длины прогнозирования", command=cl7)
btn2.place(x=0,y=80)


inp2 = Entry()

inp2.place(x=200, y =80)

btn7 = ttk.Button(text="Ввод длины данных", command=cl2)
btn7.place(x=0,y=120)


inp3 = Entry()

inp3.place(x=200,y=120)

btn11 = ttk.Button(text="Ввод", command=clvv)
btn11.place(x=200,y=160)

btn3= ttk.Button( text="МНК", command=clmnk)

btn3.place(x=0,y=160)

btn4= ttk.Button( text="Метод Берга", command=clberg)

btn4.place(x=0,y=200)


btn5= ttk.Button( text="Метод Фурье", command=clfur)

btn5.place(x=0,y=240)


btn6= ttk.Button( text="МНК с выбором функций", command=vibor)

btn6.place(x=0,y=280)

btnfur = ttk.Button(text="Глубина метода Фурье", command=clfur2)
btnfur.place(x=0, y=320)

inp4 = Entry()
inp4.place(x=200, y=320)

btnberg = ttk.Button(text="К-во коэф-ов метода Берга", command=clberg2)
btnberg.place(x=0, y=360)

inp5 = Entry()
inp5.place(x=200, y=360)

btnberg = ttk.Button(text="Кол-во перебираемых ф-ий МНК", command=cllmnk)
btnberg.place(x=0, y=400)

inp10 = Entry()
inp10.place(x=200, y=400)

btnberg = ttk.Button(text="Выбор файла", command=openf)
btnberg.place(x=0, y=440)

l1 = ttk.Label(text="Путь к файлу " + nameFile )
l1.place(x = 500, y= 10)

l2 = ttk.Label(text="Длина данных " +  str(progn))
l2.place(x = 500, y= 40)

l3 = ttk.Label(text="Длина прогнозирования " + str(l) )
l3.place(x = 500, y= 70)

l4 = ttk.Label(text="Название столбца " + str(nameofcolomn) )
l4.place(x = 500, y= 100)


l6 = ttk.Label(text="Список функций: " + str(funl) )
l6.place(x=0,y=700)

#l7 = ttk.Label(text="Ошибки" )
#l7.place(x=100,y=800)

root = mainloop()
