# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prevmap = {}

      for i , n in enumerate(nums):
        diff = target - n 
        if diff in prevmap:
          return (prevmap[nums],i)
        prevmap[n] = i
