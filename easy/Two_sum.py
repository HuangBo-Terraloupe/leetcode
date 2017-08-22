import numpy as np


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nb_terms = len(nums)
        if nb_terms <= 1:
            print "The length error"

        for i in range(nb_terms):
            look_num = target - nums[i]
            for j in range(nb_terms-i-1):
                if look_num == nums[j+i+1]:
                    return [i,j+i+1]


if __name__ == "__main__":

    two_sum = Solution()
    print two_sum.twoSum(nums=[2, 7, 11, 15], target=9)


