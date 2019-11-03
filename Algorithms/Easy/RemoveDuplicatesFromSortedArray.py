class Solution:
    def removeDuplicates(self, nums) -> int:
        total = len(nums)
        i = 0
        while i < total:
            num = nums[i]
            if num in nums[i+1:total]:
                nums.remove(num)
                total -= 1
            else:
                i += 1
        return len(nums)
s = Solution()
nums = [1,1,2]
s.removeDuplicates(nums)