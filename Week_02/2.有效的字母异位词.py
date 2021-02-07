#!/usr/bin/env python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter 
        sSet = Counter(list(s))
        tSet = Counter(list(t))
        if sSet == tSet:
            return True
        return False

