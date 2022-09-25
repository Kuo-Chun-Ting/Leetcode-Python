class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        value_to_index_dict = dict()
        for i in range(len(nums)):
            value = nums[i]
            complement = target - nums[i]
            if complement in value_to_index_dict:
                return [i, value_to_index_dict[complement]]
            value_to_index_dict[value] = i
        return []
