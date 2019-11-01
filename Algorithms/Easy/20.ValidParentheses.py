class Solution:
    def isValid(self, brackets: str) -> bool:
        stack = list()
        lookup = {"{":"}","[":"]","(":")"}
        for b in brackets:
            if b == "{" or b == "[" or b == "(":
                stack.append(b)
            else:
                if stack:
                    start = stack.pop()
                    if lookup[start] == b:
                        pass
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
                
s = Solution()
s.isValid("{(){[][]}}")