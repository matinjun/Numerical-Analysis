import numpy as np
from scipy import integrate


def romberg(f, a, b, n=10):
    """龙贝格积分，f: 函数, x in [a, b]，返回积分值和积分矩阵T"""
    # 初始化条件
    m = 0
    h = b - a
    T = [[0.5 * h * (f(a) + f(b))]]
    T[0] = np.array(T[0])
    x = np.array([a, b])

    m += 1
    while True:
        # 计算T[m][0]
        # 首先给出第m行空间，计算初始值T[m][0]
        T.append(np.zeros(m + 1))
        T[m][0] = 0.5 * T[m-1][0]
        # 划分区间宽度减半
        h = 0.5 * h
        # 计算新的取值点，并计算T[m][0]
        xx = np.zeros(2 * len(x) - 1)
        xx[0] = x[0]
        cnt = 1
        for i in range(1, len(x)):
            # 添加中点
            xx[cnt] = 0.5 * (x[i - 1] + x[i])
            T[m][0] += h * f(xx[cnt])
            cnt += 1
            # 添加原来的点
            xx[cnt] = x[i]
            cnt += 1
        x = xx

        c0 = 4 ** m / (4 ** m - 1.0)
        c1 = 1.0 / (4 ** m - 1.0)
        for k in range(1, m + 1):
            T[m][k] = c0 * T[m][k - 1] - c1 * T[m - 1][k - 1]
        # 终止条件
        if m >= n:
            break

        # m迭代加一
        m += 1
    return T[-1][-1], T


def f(x):
    if x == 0.:
        return 0
    return x ** 0.5 * np.log(x)


s, T = romberg(f, 0.0000001, 1)
res = integrate.romberg(f, 0, 1)
print(s)
print(res)
for i in range(len(T)):
    print(T[i])
