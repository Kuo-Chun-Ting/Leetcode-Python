class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a)
        b_int = int(b)
        sum_int = a_int + b_int
        sum_str = str(sum_int)
        
        answer = ''
        carry = 0
        
        for i in range(len(sum_str)-1, -1 , -1):
            sum = carry + int(sum_str[i]) 
            if sum > 1:
                answer = str(sum - 2) + answer
                carry = 1
            else:
                answer = str(sum) + answer
                carry = 0
                
        if carry == 1:
            answer = '1' + answer
            
        return answer
            
        
        
s = Solution()
print(s.addBinary("1111","11"))