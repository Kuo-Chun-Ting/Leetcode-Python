from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        if l == 0:
            return 0
        index = 0
        try:
            index = nums.index(val)
        except:
            return l
        count = 1
        for i in range(index + 1, l):
            if nums[i] != val:
                temp = nums[i]
                nums[i] = nums[index]
                nums[index] = temp
                index += 1
            else:
                count += 1
        return l - count 
                
s = Solution()
s.removeElement([22],3)