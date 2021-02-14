
#!/usr/bin/env python

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         cutoff = round(len(nums)/2)
#         from collections import Counter
#         cnterobj = Counter(nums)
#         # lt_cutoff = [x for x,cnt in cnterobj.items() if cnt>cutoff]
#         return max(cnterobj.keys(), key=lambda x: cnterobj[x])
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        count = 0
        
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count = count + 1
            else:
                count = count - 1

        return major


