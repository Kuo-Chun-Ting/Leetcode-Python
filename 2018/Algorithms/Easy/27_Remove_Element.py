from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        if l == 0:
            return 0
        
        index = -1
        count = 1
        
        for i in range(l):
            if index >= 0:
                if nums[i] != val:
                    temp = nums[i]
                    nums[i] = nums[index]
                    nums[index] = temp
                    index += 1
                else:
                    count += 1
            else:
                if nums[i] == val:
                    index = i
        if index >= 0:
            return l - count 
        else:
            return l
                
s = Solution()
s.removeElement([0,1,2,2,3,0,4,2],2)