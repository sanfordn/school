class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = []
        best.append(nums[0])

        for i in range(1,len(nums)):
            best.append(max( nums[i],
                             nums[i] + best[index[-1]))

        return best(max)
                                            """
