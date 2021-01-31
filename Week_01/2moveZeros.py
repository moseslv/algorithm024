#!/usr/bin/env python

#LINK: https://leetcode-cn.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        
        # for i in range(j+1,len(nums)):
        #     nums[i] =0

# 1遍：progress 50%