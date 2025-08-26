#
#Data structures: training on LeetCode problems
#

#1. Two Sums
from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in myMap:
                return [myMap[diff], ind]
            myMap[val] = ind
        return []
    
L = Solution1()
print(L.twoSum(nums = [2,7,11,15], target = 9))

#121. Best Time to Buy and Sell Stock

# class Solution121:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxProfit = 0
#         minProfit = prices[0]
#         diff = 0
#         temp = 0
#         for i in range(len(prices)):
#             if temp - prices[i] > 0:#-7,6
#                 if minProfit > prices[i]:#6
#                     minProfit = prices[i]
#                     maxProfit = prices[i]
#             else: 
#                 if maxProfit < prices[i]:
#                     maxProfit = prices[i]
#             temp = prices[i] #7,
#             if diff < (maxProfit - minProfit):
#                 diff = maxProfit - minProfit
#         return diff

class Solution121:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minProfit = float('inf')

        for price in prices:
            if price < minProfit:
                minProfit = price
            profit = price - minProfit

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit

A = Solution121()
print("answer: ", A.maxProfit(prices = [7,1,5,3,6,4]))

#189. Rotate Array

#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]
class Solution189:
    def rotate(self, nums: List[int], k: int) -> None:
        
        # k %= len(nums)
        # for i in range(k):
        #     temp = nums.pop()
        #     print(temp)
        #     nums.insert(0, temp)
        
        k %= len(nums)
        nums.reverse()
        first = nums[:k]
        second = nums[k:]
        first.reverse()
        second.reverse()
        nums = first + second
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)

B = Solution189()
B.rotate(nums = [1,2,3,4,5,6,7], k = 3)

#125

#3

#20

#115

#232

#739

#206

#21

#141

#2

#104

#226

#543

#235

#297

#217

#49

#347

#128

#200

#133

#207

#127

#146

#208

#295