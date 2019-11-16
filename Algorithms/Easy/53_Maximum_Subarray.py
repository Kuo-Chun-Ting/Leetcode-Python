from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = curr = nums[0]
        for i in range(1, len(nums)):
            if curr > 0:
                curr = curr + nums[i] 
            else:
                curr = nums[i]
            maximum = max(curr, maximum)
        return maximum
        
s = Solution()
print(s.maxSubArray([1]))

