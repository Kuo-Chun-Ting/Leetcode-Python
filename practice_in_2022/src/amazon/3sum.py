class TwoPointersSolution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets: list[list[int]] = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i != 0 and nums[i - 1] == nums[i]:
                continue

            low, high = i + 1, len(nums) - 1

            while low < high:
                new_sum = nums[i] + nums[low] + nums[high]
                if new_sum < 0:
                    low += 1
                elif new_sum > 0:
                    high -= 1
                else:
                    triplets.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low - 1] == nums[low]:
                        low += 1
        return triplets


class HashMapSolution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i != 0 and nums[i - 1] == nums[i]:
                continue

            value_set = set()
            j = i + 1
            while j < len(nums):
                complement = -(nums[i] + nums[j])
                if complement in value_set:
                    res.append([nums[i], nums[j], complement])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                value_set.add(nums[j])
                j += 1
        return res
