class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        
        if length == 0:
            return 0
        
        last_length = 0
        
        for i in range(length):
            if s[i] != ' ':
                last_length = last_length + 1
            if s[i] == ' ' and i+1 < length and s[i+1] != ' ':
                last_length = 0
        return last_length
            
s = Solution()
print(s.lengthOfLastWord('a aun'))