from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums), 1):
            for j in range(len(nums)-1, i, -1):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
                if j-1 == i:
                    break
        return None
