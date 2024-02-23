"""
Leetcode two sum problem
"""


class TwoSum(object):
    """
    Leetcode Two sum problem class
    """

    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target

    def two_sum(self):
        """
        Returns the indices of two sum

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices: list[int] = []
        for i in range(len(self.nums)):
            j = i + 1
            while j < len(self.nums):
                if self.nums[i] + self.nums[j] == self.target:
                    indices.append(i)
                    indices.append(j)
                j += 1
        return indices


solution = TwoSum([11, 7, 13, 15, 6, 12, 8, 14, 9], 25)

result = solution.two_sum()

print(result)
