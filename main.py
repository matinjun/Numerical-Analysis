# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def hernor_Qin_jiusao(x, nums):
    """利用秦九韶法求多项式值，nums为系数部分，按降序排列"""
    b = nums[0]
    for i in range(1, len(nums)):
        b = b * x + nums[i]
    return b


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
        a[k] /= omica

    def f(xi):
        b = np.ones(len(x))
        b *= xi
        b = 1.0 / (b - x)
        omica = 1.0
        for k in range(len(x)):
            omica *= (xi - x[k])
        b *= omica
        return np.sum(a * b)
    return f


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    x = int(input("请输入x: "))
    nums = input("请输入系数部分: ").split()
    nums = [int(num) for num in nums]
    print("答案是: " + str(hernor_Qin_jiusao(x, nums)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
