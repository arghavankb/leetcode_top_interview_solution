class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p_write = n + m - 1
        p_nums1 = m - 1
        p_nums2 = n - 1

        if n==0:
            return nums1
        if m == 0:
            nums1[:n] = nums2
            return nums1

        while p_nums1 >= 0 and p_nums2 >= 0:
            if nums1[p_nums1] > nums2[p_nums2]:
                nums1[p_write] = nums1[p_nums1]
                p_write -= 1
                p_nums1 -= 1

            else:
                nums1[p_write] = nums2[p_nums2]
                p_write -= 1
                p_nums2 -= 1

        while p_nums2>=0:
            nums1[p_write] = nums2[p_nums2]
            p_write -= 1
            p_nums2 -= 1

        return nums1
