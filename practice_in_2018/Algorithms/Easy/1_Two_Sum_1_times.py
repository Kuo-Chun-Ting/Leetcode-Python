from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in dic:
                return [i , dic[key]]
            else:
                dic[nums[i]] = i
        return []
    
s = Solution()
s.twoSum([3,3],6)