import numpy as np
import numpy.random as rn
from matplotlib.pyplot import plot
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def Lagrange(x, y):
    """返回一个插值函数"""
    # 计算插值函数的系数部分
    # a0, a1, a2, ... 初始值为y0, y1, ...
    a = np.array(y)
    for k in range(len(x)):
        omica = 1.0
        for j in range(len(x)):
            if j != k:
                omica *= (x[k] - x[j])
        # 最终每个系数为yk / omica
        a[k] /= omica

    def f(xi):
        yi = 0.0
        for k in range(len(x)):
            bk = 1.0
            for j in range(len(x)):
                if j != k:
                    bk = bk * (xi - x[j])
            bk = bk * a[k]
            yi += bk
        return yi

    return f


def Newton(x, y):
    """返回一个Newton插值函数"""
    a = np.zeros(len(x))
    a[0] = y[0]
    # 系数表t
    t = np.zeros((len(x), len(x)))
    for i in range(len(x)):
        t[i][0] = y[i]
    # 计算系数部分
    # 后面系数部分的计算误差会越来越大（在数据较多的情况下）
    for j in range(1, len(x)):
        for i in range(j, len(x)):
            t[i][j] = (t[i][(j - 1)] - t[i - 1][(j - 1)]) / (x[i] - x[i - j])
        a[j] = t[j][j]

    def f(xi):
        """根据xi计算近似值"""
        yi = 0.0
        for i in range(len(x)):
            bi = 1.0
            j = 0
            while j < i:
                bi = bi * (xi - x[j])
                j = j + 1
            yi = yi + a[i] * bi
        return yi
    return f


def interpolate_line(X, Y):
    """分段线性插值"""

    def f(x):
        for i in range(len(X) - 1):
            if X[i] <= x and x <= X[i + 1]:
                return Y[i] * (x - X[i + 1]) / (X[i] - X[i + 1]) +\
                       Y[i + 1] * (x - X[i]) / (X[i + 1] - X[i])
        return "x is out of range!"
    return f


# x = np.array([0.40, 0.55, 0.65, 0.80, 0.90, 1.05])
# y = np.array([0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382])
def test_newton_lagrange(step):
    x = np.linspace(-np.pi, np.pi, 200)
    y = np.sin(x)
    xx = x[::step]
    yy = y[::step]
    Newt = Newton(xx, yy)
    yn = Newt(x)
    Lag = Lagrange(xx, yy)
    yl = Lag(x)

    n = 70
    plot(x, y, 'b', x, yn, 'r', x, yl, 'g--')
    plt.show()


def test_interpolate_line(n=40):
    """测试在n个点情况下的线性分段插值"""
    x = np.linspace(-5, 5, 200)
    y = 1.0 / (1.0 + x ** 2)

    xx = np.linspace(-5, 5, n)
    yy = 1.0 / (1.0 + xx ** 2)
    f = interpolate_line(xx, yy)
    yf = [f(v) for v in x]
    yf = np.array(yf)

    cubic = interp1d(xx, yy, kind='cubic')
    plot(x, y, 'r', x, yf, 'b', x, cubic(x), 'k')


test_interpolate_line(20)
