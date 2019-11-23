from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        length = len(digits)
        carry = 0
        sum = digits[length - 1] + 1
        
        if sum >= 10:
            digits[length - 1] = sum - 10
            carry = 1
        else:
            digits[length - 1] = digits[length - 1] + 1
            return digits
        
        for i in range(length - 2, -1, -1):
            if carry + digits[i] >= 10:
                digits[i] = digits[i] + carry - 10
                carry = 1
            else:
                digits[i] = digits[i] + 1
                carry = 0
                return digits
            
        if carry != 0:
            digits.insert(0,1)
            
        return digits
        
s = Solution()
print(s.plusOne([9]))