import numpy as np
from matplotlib.pyplot import plot


def norm(p, color='b'):
    """画出p范数"""
    x = np.linspace(0, 1, 200)
    y = (1 - x ** p) ** (1.0 / p)
    _x = -x
    _y = -y
    plot(x, y, color, x, _y, color, _x, y, color, _x, _y, color)


if __name__ == 'n_norm.py':
    norm(1)
