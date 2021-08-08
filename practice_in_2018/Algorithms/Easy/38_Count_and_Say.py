class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        nums = self.countAndSay(n-1)
        current = nums[0]
        count = 1
        result = ""
        for i in range(1, len(nums)):
            if nums[i] == current:
                count += 1
            else:
                result += str(count) + str(current)
                current = nums[i]
                count = 1
        result += str(count) + str(current)
        
        return result
s = Solution()
print(s.countAndSay(00))