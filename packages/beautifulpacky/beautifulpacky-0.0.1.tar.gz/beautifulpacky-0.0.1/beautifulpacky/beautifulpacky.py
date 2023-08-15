"""
    这是一个示例库，提供了一个用于计算阶乘的函数。
"""


def calculate_factorial(n):
    """
    计算给定数值的阶乘。

    参数：
        n (int): 需要计算阶乘的非负整数。

    返回：
        int: 给定数值的阶乘结果。

    异常：
        ValueError: 如果输入的数值不是非负整数。

    示例：
        >>> calculate_factorial(5)
        120
    """
    # 函数实现...


def calculate_factorial(n):
    """计算给定数值的阶乘"""
    if n < 0:
        raise ValueError("输入的数值必须是非负整数")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
