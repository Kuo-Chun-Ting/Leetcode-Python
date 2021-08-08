from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        shortest = strs[0];
        l = len(strs[0])
        
        for i in range(1, len(strs)):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]
                l = len(strs[i])
                
        for i in range(len(shortest)):
            comStr = shortest[0: l-i]
            isCommon = True
            for s in strs:
                if s.startswith(comStr):
                    pass
                else:
                    isCommon = False
                    break
            if isCommon:
                return comStr
                
        return "";
s = Solution()
s.longestCommonPrefix(["flower","flow","flight"])