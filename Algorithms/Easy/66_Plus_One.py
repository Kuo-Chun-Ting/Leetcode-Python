from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        toStr = ''.join(str(i) for i in digits)
        toInt = int(toStr)
        toInt += 1
        result = [int(i) for i in str(toInt)]
        return result
        
s = Solution()
print(s.plusOne([9,2,3,4]))