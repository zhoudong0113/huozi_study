
#定义一个计算器类
import pytest


class Calculator(object):

    # 加法

    def add(self, a, b):
        return a + b

    # 减法
    def sub(self, a, b):
        return a - b

    # 乘法
    def mul(self, a, b):
        return a * b

    # 除法
    def div(self, a, b):
        return a / b