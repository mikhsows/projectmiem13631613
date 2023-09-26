import numpy as np
import pandas as pd
import sympy as sp
import random
import math



def ed(i):
    return 1

def sq3(a):
    return a**(1/3)


def cos3x(a):
    return np.cos(3*a)

def cos2x(a):
    return np.cos(2*a)

def sin2x(a):
    return np.sin(2*a)

def sin3x(a):
    return np.sin(3*a)


def x4(a):
    return a**4

def xm2(a):
    if a!=0:
        return (a)**(-2)
    else:
        return  0

def expm(a):
    if a!=0:
        return np.exp(-a)
    else:
        return 0

def lgm(a):
    if a!=0:
        return np.log(1/(a))
    else:
        return 0

def ed(i):
    return 1

def sq(i):
    return i**2

def kub(i):
    return i**3

def ob(i):
    if i!=0:
        return (i)**(-1)
    else:
        return  0

def pokv2(i):
    return 2**i

def pokn2(i):
    return 2**(-i)

def ns(i):
    return i

def log(i):
    if i!=0:
        return np.log(i)
    else:
        return  0

def mls(funlist, mmax, mmin, d, d1, coor, coor2):
    x = []
    for i in range(len(funlist)):
        x.append(sp.symbols("C" + str(i + 1)))

    su = 0
    for i in range(len(d)):
        kv = 0
        for j in range(len(x)):
            kv = kv + x[j] * funlist[j](coor2[i] )
        su = su + (kv - d[i]) ** 2
    di = []
    for i in range(len(x)):
        di.append(sp.diff(su, x[i]))
    resh = sp.solve(di, x)
    mat2 = np.zeros((len(x), len(x)))
    for i in range(len(x)):
        for j in range(len(x)):
            for g in range(len(d)):
                mat2[i, j] = mat2[i, j] + 2 * funlist[i](d[g]) * funlist[j](coor2[g])

    progn = len(d1)  # кол-во итераций для предсказания
    flag2 = 1
    results = np.zeros(progn)
    for i in range(progn):
        for j in range(len(resh)):
            results[i] = results[i] + resh[x[j]] * funlist[j](coor[i])
        if (results[i] < mmin or results[i] > mmax):
            flag2 = 0

    for i in range(len(x) - 1):
        if (np.linalg.det(mat2[0:i + 1, 0:i + 1]) < 0):
            flag2 = 0


    sumo = 0
    for i in range(progn):
        sumo = sumo + abs(d1[i] - results[i])

    return sumo, x, resh, flag2

def runmnk(dk, progn, numoftests):
    k = 0
    for i in range(len(dk)):
        k = k + dk[i]
    k = k / len(dk)
    dis = 0
    for i in range(len(dk)):
        dis = dis + (dk[i] - k) ** 2
    dis = dis / (len(dk) - 1)
    mmax = k + 3 * np.sqrt(dis)
    mmin = k - 3 * np.sqrt(dis)
    funlist = [np.cos, np.sin, ed, log, sq, kub, ob, pokn2, sq3, cos3x, cos2x, sin3x, sin2x]
    x = []
    for i in range(len(funlist)):
        x.append(sp.symbols("C" + str(i + 1)))
    p = len(dk) // 4
    p1 = p * 3 + len(dk) % 4
    de1 = np.zeros(p1)
    de2 = np.zeros(p)
    cr1 = np.zeros(p1)
    cr2 = np.zeros(p)
    j = 0
    g = 0
    for i in range(len(dk)):
        if ((i + 1) % 4 == 0):
            de2[j] = dk[i]
            cr2[j] = i
            j = j + 1
        else:
            de1[g] = dk[i]
            cr1[g] = i
            g = g + 1
    #numoftests = 5
    mino = 1000000000
    # mino,minox,minoresh = mls(funlist, mmax,mmin,de1,de2,cr2,cr1)
    nab = funlist
    for i in range(numoftests):
        a= math.ceil(random.random()*len(funlist))
        funcs = (random.sample(funlist, a))
        #funcs.append(ed)
        m, x, resh, flag = mls(funcs, mmax, mmin, de1, de2, cr2, cr1)
        flag2 = 1
        results = np.zeros(progn)
        for i in range(progn):
            for j in range(len(resh)):
                results[i] = results[i] + resh[x[j]] * funcs[j](i + len(dk))
            if (results[i] < mmin or results[i] > mmax):
                flag2 = 0
        if (m < mino and flag2!=0 and flag!=0):
            mino = m
            minox = x
            minoresh = resh
            nab = funcs

    flag2 = 1
    results = np.zeros(progn)
    for i in range(progn):
        for j in range(len(minoresh)):
            results[i] = results[i] + minoresh[minox[j]] * nab[j](i + len(dk))
        if (results[i] < mmin or results[i] > mmax):
            flag2 = 0


    df = pd.DataFrame(results)
    df.to_csv("result.csv", header=False)
    #np.savetxt("results.txt", results)

    preresults = np.zeros(len(dk) + progn)
    for i in range(len(preresults)):
        for j in range(len(minoresh)):
            preresults[i] = preresults[i] + minoresh[minox[j]] * nab[j](i)
    return preresults, flag2
