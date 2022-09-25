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


class NoSortSolution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res, dups = set(), set()

        # Instead of re-populating a hashset every time in the inner loop as line 41 above,
        # we can use a hashmap and populate it once.
        seen = {}

        for i in range(len(nums)):
            if nums[i] not in dups:
                dups.add(nums[i])

                for j in range(i + 1, len(nums)):
                    complement = -(nums[i] + nums[j])
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted([nums[i], nums[j], complement])))

                    # Values in the hashmap will indicate whether we have encountered that element in the current iteration i
                    seen[nums[j]] = i
        return res


if __name__ == "__main__":
    input = [-1, 0, 1, 2, -1, -4]
    res = NoSortSolution().threeSum(input)
    print(res)
