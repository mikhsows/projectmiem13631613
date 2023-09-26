import numpy as np
import pandas as pd
import sympy as sp


def runmnkw2(d, funlist, progn):
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

    x = []
    for i in range(len(funlist)):
        x.append(sp.symbols("C" + str(i + 1)))

    su = 0
    for i in range(len(d)):
        kv = 0
        for j in range(len(x)):
            kv = kv + x[j] * funlist[j](i + 1)
        su = su + (kv - d[i]) ** 2
    di = []
    for i in range(len(x)):
        di.append(sp.diff(su, x[i]))
    resh = sp.solve(di, x)
    mat2 = np.zeros((len(x), len(x)))
    for i in range(len(x)):
        for j in range(len(x)):
            for g in range(len(d)):
                mat2[i, j] = mat2[i, j] + 2 * funlist[i](d[g]) * funlist[j](d[g])

    flag2 = 1
    results = np.zeros(progn)
    for i in range(progn):
        for j in range(len(resh)):
            results[i] = results[i] + resh[x[j]] * funlist[j](i + len(d))
        if (results[i] < mmin or results[i] > mmax):
            flag2 = 0

    for i in range(len(x) - 1):
        if (np.linalg.det(mat2[0:i + 1, 0:i + 1]) < 0):
            flag2 = 0



    df = pd.DataFrame(results)
    df.to_csv("result.csv", header=False)
    #np.savetxt("results.txt", results)

    preresults = np.zeros(len(d) + progn)
    for i in range(len(preresults)):
        for j in range(len(resh)):
            preresults[i] = preresults[i] + resh[x[j]] * funlist[j](i)
    return preresults, flag2



