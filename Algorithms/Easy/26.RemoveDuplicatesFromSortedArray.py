class Solution:
    def removeDuplicates(self, nums) -> int:
        l = len(nums)
        if l == 0:
            return 0
        i = 0
        for j in range(1, l):
            if nums[i] != nums[j]:
                temp =nums[i+1]
                nums[i+1] = nums[j]
                nums[j] = temp
                i += 1
        return i + 1
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
s.removeDuplicates(nums)