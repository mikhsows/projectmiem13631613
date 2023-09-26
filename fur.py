import numpy as np
import pandas as pd

def fz(size,y):
    zero_coef=0
    for i in range(size):
        zero_coef += y[i]
    zero_coef /= size
    return zero_coef



def fc(tmp, moda, size):
    coefs = np.zeros(2)
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    tmp4 = 0
    tmp5 = 0
    for i in range(size):
        tmp1 += np.sin(moda * i) ** 2
        tmp2 += np.cos(moda * i) * np.sin(moda * i)
        tmp3 += tmp[i] * np.sin(moda * i)
        tmp4 += np.cos(moda * i) ** 2
        tmp5 += tmp[i] * np.cos(moda * i)

    coefs[0] = (tmp5 * tmp1 - tmp2 * tmp3) / (tmp4 * tmp1 - tmp2 ** 2)
    coefs[1] = (tmp3 - coefs[0] * tmp2) / tmp1
    return coefs


def run( y, a, b, zero_coef, depth, size):
    sch = 1
    rez = np.zeros(depth * 2 + 1)
    tmp = np.zeros(size)
    rez[0] = zero_coef
    for z in range(depth):
        for j in range(size):
            tmp[j] = zero_coef

        for i in range(z):

            for j in range(size):
                tmp[j] += a[i] * np.cos((i + 1) * j) + b[i] * np.sin((i + 1) * j)

        for j in range(size):
            tmp[j] = y[j] - tmp[j]

        coefs = fc(tmp, z + 1,  size)
        a[z] = coefs[0]
        b[z] = coefs[1]
        rez[sch] = coefs[0]
        rez[sch + 1] = coefs[1]
        sch = sch + 2
    return (rez,a, b)


def show( a, b, zero_coef, depth, size):
    tm = np.zeros(size)
    for j in range(size):
        tmp = zero_coef
        for l in range(depth):
            tmp += a[l] * np.cos((l + 1) * j) + b[l] * np.sin((l + 1) * j)
        tm[j] = tmp
    return tm


def show2(size,a,b,zero_coef,depth,pr):
    tm2 = np.zeros(pr)
    pr1 = np.linspace(1,pr,pr)
    for j in range(pr):
        tmp = zero_coef
        for l in range(depth):
            tmp += a[l]*np.cos((l + 1)*(size+pr1[j])) + b[l]*np.sin((l + 1)*(size+pr1[j]))
        tm2[j]=tmp
    return tm2

def fun( y, size, depth, pr):
    a = np.zeros(depth)
    b = np.zeros(depth)
    zero_coef = fz(size, y)

    rez,a,b = run(y,a,b,zero_coef,depth,size)
    tm=show(a,b,zero_coef,depth,size)
    tm2 = show2(size,a,b,zero_coef,depth,pr)
    return tm,tm2

def runfur(d, progn, fff):
    p,p1=fun(d,len(d),fff,progn)

    k = 0
    for i in range(len(d)):
        k = k + d[i]
    k = k / len(d)
    dis = 0
    for i in range(len(d)):
        dis = dis + (d[i] - k) ** 2
    dis = dis / (len(d) - 1)
    mmax = k + 3 * np.sqrt(dis)
    mmin = k - 3 * np.sqrt(dis)
    flag2 = 1
    for i in range(len(p1)):
        if (p1[i] < mmin or p1[i] > mmax):
            flag2 = 0
    df = pd.DataFrame(p1)
    df.to_csv("result.csv", header=False)
    #np.savetxt("results.txt", p1)
    p=np.concatenate((p,p1))
    return p,flag2