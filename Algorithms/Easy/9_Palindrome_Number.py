class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse = x[::-1]
        if x == reverse:
            return True
        else:
            return False
        
s = Solution()
s.isPalindrome(1234223)