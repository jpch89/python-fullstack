"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

# Python 2.7.3
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1: return 1
        if number == 2: return 2
        n = 2
        result = 0
        a = 1
        b = 2
        while n != number:
            a, b = b, a + b
            n += 1
        return b

"""
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 1:
            return 0

        if number == 1:
            return 1

        if number == 2:
            return 2

        ret = 0
        a = 1
        b = 2
        for i in range(3, number+1):
            ret = a + b
            a = b
            b = ret
        return ret
"""
