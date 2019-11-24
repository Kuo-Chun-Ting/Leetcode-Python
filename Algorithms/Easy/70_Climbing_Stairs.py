class Solution:
    def climbStairs(self, n: int) -> int:
        solutions = [1, 2]
        
        for i in range(2, n):
            ways = solutions[i-1] + solutions[i-2]
            solutions.append(ways)
            
        return solutions[n-1]
s = Solution()
print(s.climbStairs(3))