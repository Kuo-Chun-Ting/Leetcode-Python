from typing import List


class HorizontalScanningSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for i in range(len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]
                if not prefix:
                    return ""
        return prefix


class VerticalScanningSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""

        first_str = strs[0]
        for i in range(len(first_str)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or first_str[i] != strs[j][i]:
                    return strs[0][:i]

        return first_str


class DivideAndConquerSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""

        return self.longest_common_prefix_in_range(strs, 0, len(strs)-1)

    def longest_common_prefix_in_range(self, strs: List[str], left: int, right: int):
        if left == right:
            return strs[left]

        mid = (left + right) // 2
        left_lcp = self.longest_common_prefix_in_range(strs, left, mid)
        right_lcp = self.longest_common_prefix_in_range(strs, mid+1, right)
        return self.common_prefix(left_lcp, right_lcp)

    def common_prefix(self, left: str, right: str):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[0:i]

        return left[0:min_len]


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(HorizontalScanningSolution().longestCommonPrefix(strs))
    print(VerticalScanningSolution().longestCommonPrefix(strs))
    print(DivideAndConquerSolution().longestCommonPrefix(strs))
