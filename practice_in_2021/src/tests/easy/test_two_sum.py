import pytest

from easy.two_sum import Solution

@pytest.mark.parametrize("nums,target,expected", [
    ([2,7,11,15], 9, [0,1]), ([3,2,2,3], 6, [0,3]), ([2,1,1,2], 2, [1,2])
])
def test_twoSum(nums, target, expected):
    # Act
    result = Solution().twoSum(nums, target)

    # Assert
    assert result == expected