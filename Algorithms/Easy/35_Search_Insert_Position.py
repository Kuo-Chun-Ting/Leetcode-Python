from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        if l == 0:
            return 0
        j = -1
        for i in range(l):
            if nums[i] < target:
                j = i
            elif nums[i] == target:
                return i
            elif nums[i] > target:
                if j != -1:
                    return i
                else:
                    return 0
        if j == l - 1:
            return l 
s = Solution()
s.searchInsert([], 0)