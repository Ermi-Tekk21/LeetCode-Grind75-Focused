class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)  # If more than one zero, all elements in the result are 0.

        pre_mul = [1]  # Start with 1 instead of nums[0] to handle edge cases.
        zero_at = -1  # Initialize zero index to -1 (indicating no zero).

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_at = i
                continue  # Skip multiplying zero to avoid incorrect pre_mul values.
            pre_mul.append(pre_mul[-1] * nums[i])

        if zero_at != -1:  # If there's exactly one zero
            result = [0] * len(nums)
            result[zero_at] = pre_mul[-1]  # Only the zero index should have a product value.
            return result

        # Compute product for non-zero elements
        return [int(pre_mul[-1] / nums[i]) for i in range(len(nums))]