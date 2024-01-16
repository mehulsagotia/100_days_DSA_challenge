# ques - 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
          # Sort the list first
        nums.sort()

        i = 0
        while i < len(nums) - 1:
            currNum = nums[i]
            nextNum = nums[i+1]
            if currNum == nextNum:
                return True

            i += 1

        return False
