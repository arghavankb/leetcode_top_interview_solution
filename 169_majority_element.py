class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = {}
        half_len = len(nums) / 2

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        max_key = max(counter, key=counter.get)
        max_value = counter[max_key]

        if max_value > half_len:
            return max_key






