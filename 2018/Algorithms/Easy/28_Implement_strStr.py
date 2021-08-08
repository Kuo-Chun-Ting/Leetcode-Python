class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            index = haystack.index(needle)
            return index
        except:
            return -1
s = Solution()
s.strStr("hello","ll3")