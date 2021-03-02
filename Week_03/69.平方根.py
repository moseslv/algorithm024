#!/usr/bin/env python

# 根据牛顿法迭代求解

class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0.1
        while abs(res ** 2 - x) > 1e-05:    
            res = (res + x / res) / 2
        return int(res)

