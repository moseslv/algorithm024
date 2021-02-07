#!/usr/bin/env python

# class Solution:
#     # 哈希表，映射求解
#     # O（n^2）
#     def groupAnagrams(self, strs):
#         charList = [list(x) for x in strs]
#         charAscisum = list(map(self.transAsci,charList))
#         returnList = []
#         for i in set(charAscisum):
#             setList = []
#             for idx,val in enumerate(charAscisum):
#                 if i == val :
#                     setList.append(strs[idx])
#             returnList.append(setList)
#         return returnList
    
#     def transAsci(self,Listchar):
#         return sum(ord(x)**4 for x in Listchar)
# 50% 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            d.setdefault( "".join(sorted(s)), []).append(s)
        return list(d.values())