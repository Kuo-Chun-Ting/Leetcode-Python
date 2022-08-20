from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer_pairs = dict()
        for i in range(len(nums)):
            if nums[i] in answer_pairs:
                return [answer_pairs[nums[i]], i]
            else:
                answer_pairs[target-nums[i]] = i
