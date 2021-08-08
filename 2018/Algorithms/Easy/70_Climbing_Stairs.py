class Solution:
    # by Dynamic Programing
    # sum solutions from 0 to n
    def climbStairs(self, n: int) -> int:
        solution_table = [1, 2]
        
        for i in range(2, n):
            solution = solution_table[i-1] + solution_table[i-2]
            solution_table.append(solution)
            
        return solution_table[n-1]
    
s = Solution()
print(s.climbStairs(3))