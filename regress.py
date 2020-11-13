import numpy as np
from matplotlib.pyplot import plot
import matplotlib.pyplot as plt


def regress(x, y, n):
    """根据散点集，生成拟合函数regressPoly"""
    # 初始条件
    alpha = np.mean(x)
    beta = 0
    # 最终返回的结果
    regressPoly = np.poly1d([0.])

    P = []
    co = []
    #  计算出多项式P[0]和系数co[0]
    P.append(np.poly1d([1.]))
    c = np.sum(y * P[0](x)) / np.sum(P[0](x) * P[0](x))
    co.append(c)
    # 累加最终结果
    regressPoly += co[0] * P[0]

    # 计算多项式P[1]
    p = np.poly1d([1.0, -alpha]) * P[0]
    P.append(p)

    for k in range(1, n):
        # 计算系数co[k]
        c = np.sum(y * P[k](x)) / np.sum(P[k](x) * P[k](x))
        co.append(c)
        # 累加最终结果
        regressPoly += co[k] * P[k]

        # 计算alpha与beta
        alpha = np.sum(P[k](x) * (P[k] * np.poly1d([1., 0.]))(x)) / np.sum(P[k](x) * P[k](x))
        beta = np.sum(P[k](x) * P[k](x)) / np.sum(P[k - 1](x) * P[k - 1](x))
        # 计算多项式P[k + 1]
        p = np.poly1d([1.0, -alpha]) * P[k] - beta * P[k - 1]
        P.append(p)

    # 计算系数co[k]
    c = np.sum(y * P[n](x)) / np.sum(P[n](x) * P[n](x))
    co.append(c)

    # 累加最终结果
    regressPoly += co[n] * P[n]

    return regressPoly


x = np.linspace(1, 10, 20)
y = np.log(x)
xx = np.linspace(1, 10, 100)
f = regress(x, y, 4)
yy = f(xx)
# 绘画出散点数据
plt.scatter(x, y, marker="x", color="r")
# 绘画出拟合图像
plot(xx, yy)
plt.show()
