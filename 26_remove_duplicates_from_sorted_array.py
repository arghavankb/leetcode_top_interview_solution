class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        previous_num = nums[0]
        p_write = 1
        p_read = 1
        k = 1

        while p_read < len(nums):
            if nums[p_read] == previous_num:
                p_read += 1
            else:
                nums[p_write] = nums[p_read]
                previous_num = nums[p_read]
                k += 1
                p_read += 1
                p_write += 1

        return k