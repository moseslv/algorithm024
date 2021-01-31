#link： https://leetcode-cn.com/problems/two-sum/

class Solution:
    # 两层循环
    # def twoSum(self,nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i] + nums[j]==target:
    #                 return [i,j]

    # 哈希表
    def twoSum(self,nums, target):
        hasmap = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if hasmap.get(diff) is not None:
                return [hasmap.get(diff),i]     
            else:
                hasmap[nums[i]] = i

# 1rd: {2:1}
# 2rd: --> 返回【hasmap[2],i=1]