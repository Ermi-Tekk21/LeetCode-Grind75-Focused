class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize an empty list
        k_numbers_min_heap = []

        # Add first k elements to the list
        for i in range(k):
            k_numbers_min_heap.append(nums[i])

        # Convert the list into a min-heap
        heapq.heapify(k_numbers_min_heap)

        # Loop through the remaining elements in the 'nums' array
        for i in range(k, len(nums)):
            # Compare the current element with the minimum
            # element (root) of the min-heap
            if nums[i] > k_numbers_min_heap[0]:
                # Remove the smallest element
                heapq.heappop(k_numbers_min_heap)
                # Add the current element
                heapq.heappush(k_numbers_min_heap, nums[i])

        # The root of the heap has the Kth largest element
        return k_numbers_min_heap[0]
