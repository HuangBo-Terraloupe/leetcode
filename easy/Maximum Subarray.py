class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        else:
            max_sum = temp_sum = nums[0]
            for num in nums[1:]:
                temp_sum = max(num, num + temp_sum)
                max_sum = max(max_sum, temp_sum)
            return max_sum
