from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        position = 0
        for i in range(len(nums2)):
            for j in range(position, len(nums1)):
                if nums2[i] >= nums1[j] and j < len(nums1)-1 and nums1[j+1] >= nums2[i] or nums1[j+1] == 0:
                    nums1.insert(j+1,nums2[i])
                    position = j+1
                    break
        for i in range(len(nums1)-m-n):
            nums1.remove(0)
s = Solution()
nums1 = [0]
nums2 = [1]
s.merge(nums1,0,nums2,1)
print(nums1)