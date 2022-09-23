class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_table = dict()
        for i in range(len(nums)):
            val = nums[i]
            complement = target - nums[i]
            if complement in hash_table:
                return [i, hash_table[complement]]
            hash_table[val] = i
        return []