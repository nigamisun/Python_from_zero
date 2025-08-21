#
#Data structers: train on LeetCode problems
#

#1. Two Sums
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in myMap:
                return [myMap[diff], ind]
            myMap[val] = ind
        return []
    
L = Solution()
print(L.twoSum(nums = [2,7,11,15], target = 9))