class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max = 1
        substring = s[0]
        for i in range(1, len(s)):
            if s[i] in substring:
                index = substring.index(s[i])
                substring = substring[index+1:len(substring)] + s[i]
            else:
                substring += s[i]
                if len(substring) > max:
                    max = len(substring)
        return max
            
                

s = Solution()
max = s.lengthOfLongestSubstring("aabaab!bb")                