class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = s[0]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                substring += s[i]
            else:
                print("檢查下一個一不一樣")
        return substring



s = Solution()
result = s.longestPalindrome("babad")