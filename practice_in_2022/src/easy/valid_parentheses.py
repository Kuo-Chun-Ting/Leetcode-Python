class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        
        stack = []
        
        for parentheses in s:
            if parentheses in bracket_dict:
               stack.append(parentheses)
            elif not stack:
                return False
            else:
                key = stack.pop()
                if bracket_dict.get(key) == parentheses:
                    continue
                return False
            
        return stack == []