#!/usr/bin/env python


# 以动态规划的思想来完成，爬楼梯的子任务拆解
class Solution:
    def climbStairs(self, n: int) -> int:
        dp ={0:0,1:1,2:2}
        
        for i in range(3,n+1):
            dp[i] = dp[i-1] +  dp[i-2]

        return dp[n]
