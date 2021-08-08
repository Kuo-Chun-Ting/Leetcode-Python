from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        
        dic = {}
        for i in range(l):
            dic[nums[i]] = i
            
        for i in range(l):
            key = target - nums[i]
            if key in dic and dic[key] != i: 
                return [i, dic[key]]
        return []
    
s = Solution()
s.twoSum([3,3,3],6)