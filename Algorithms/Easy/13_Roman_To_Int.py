class Solution(object):
    def romanToInt(self, symbol):
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        sum = 0
        previous = -1
        reset = True
        length = len(symbol)
        
        for i in range(length):
            s = symbol[i]
            p = symbol[i - 1]
            current = dic[s]
            previous = dic[p]
                
            if reset :
                reset = False
            else:
                if previous >= current:
                    sum += previous
                else:
                    sum += current - previous
                    reset = True
            if i == length - 1:
                if reset != True:
                    sum += current
        return sum
    

s = Solution()
# print(s.romanToInt("MCMXCIV"))
# print(s.romanToInt("III"))
print(s.romanToInt("MDCXCV"))
