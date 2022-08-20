class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        left, right = 1, 1

        while left * 10 <= x:
            left *= 10

        while left > right:
            if (x//left) % 10 != (x//right) % 10:
                return False

            left /= 10
            right *= 10

        return True
