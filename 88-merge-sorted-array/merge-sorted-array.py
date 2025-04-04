class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1  # Pointers for nums1, nums2, and merged position

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:  
                nums1[k] = nums1[i]  # Move larger element to the end
                i -= 1
            else:
                nums1[k] = nums2[j]  # Place nums2 element at the correct position
                j -= 1
            k -= 1  # Move backwards