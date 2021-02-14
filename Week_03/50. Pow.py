#!/usr/bin/env python

# 50. Pow(x, n)

class Solution:

    def myPow(self, x: float, n: int) -> float:
        def inner_myPow(x, n):
            if n == 1: return x
            if n == 0: return 1
            # 定义分治后的乘积
            y = inner_myPow(x, n // 2)
            # 偶数时直接y的平方
            if n % 2 == 0: return y * y
            # 奇数时需要多乘一个x
            else: return y * y * x
        # 当指数小于0时，转出大于0再进行运算
        if n < 0: return 1 / self.myPow(x, -n)
        return inner_myPow(x, n)



# 以下解法超时
"""
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n==0:
#             return 1
#         if n==1:
#             return x
#         if n==-1:
#             return 1/x
#         rest = self.myPow(x,n%2)
#         half = self.myPow(x,n/2)
#         return rest*half*half

"""