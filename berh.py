import numpy as np
import pandas as pd

def M(xs, x, cs, coef):
    N = xs - 1
    m = cs
    Ak = np.zeros(m + 1)
    Ak[0] = 1
    f = np.copy(x)
    b = np.copy(x)
    Dk = 0
    for i in range(N+1):
        Dk += 2.0 * f[i] **2
    Dk -= f[0] **2 + b[N] **2

    for i in range(m):
        mu = 0.0
        for j in range(N-i):
            mu += f[i + j + 1] * b[j]
        mu *= -2.0 / Dk
        for n in range((i+1)//2+1):
            t1 = Ak[n] + mu * Ak[i + 1 - n]
            t2 = Ak[i + 1 - n] + mu * Ak[n]
            Ak[n] = t1
            Ak[i + 1 - n] = t2
        for n in range(N-i):
            t1 = f[n + i + 1] + mu * b[n]
            t2 = b[n] + mu * f[n + i + 1]
            f[n + i + 1] = t1
            b[n] = t2
        Dk = (1.0 - mu * mu) * Dk - f[i + 1] * f[i + 1] - b[N - i - 1] * b[N - i - 1]
    for j in range(cs):
        coef[j] = Ak[j + 1]
    return coef


def pred(n, x, xs, cs):
    res = np.zeros(n)
    coefs = np.zeros(cs)
    t = np.zeros(xs + n)
    coefs = M(xs, x, cs, coefs)
    for i in range(xs):
        t[i] = x[i]
    for i in range(xs, xs + n):
        for j in range(cs):
            t[i] = t[i]  -  coefs[j] * t[i - j - 1]
        res[i - xs] = t[i]
    return res

def runberg(d, progn, bbb):
    p = pred(progn, d, len(d), bbb)

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
    for i in range(len(p)):
        if (p[i] < mmin or p[i] > mmax):
            flag2 = 0

    df = pd.DataFrame(p)
    df.to_csv("result.csv", header=False)
    #np.savetxt("results.txt", p)
    return p, flag2