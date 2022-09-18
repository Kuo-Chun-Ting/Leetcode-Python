class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets: list[list[int]]= []
        index_set: set[tuple[int]] = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
                
            if i!=0 and nums[i-1] == nums[i]:
                continue

            low, high = i+1, len(nums)-1
            
            while low < high:
                new_sum = nums[i] + nums[low] + nums[high]
                if new_sum < 0:
                    low += 1
                elif new_sum > 0:
                    high -= 1
                else:
                    key = (nums[i], nums[low], nums[high])
                    if key not in index_set:
                        index_set.add(key)
                        triplets.append([nums[i], nums[low], nums[high]])
                    low += 1
        return triplets