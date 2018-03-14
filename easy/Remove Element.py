class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        output = 0
        for item in nums:
            if item != val:
                nums[output] = item
                output += 1
        return output
