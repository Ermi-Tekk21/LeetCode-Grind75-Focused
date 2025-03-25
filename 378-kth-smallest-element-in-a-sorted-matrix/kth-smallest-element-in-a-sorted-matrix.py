class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []

        for row in matrix:
            for num in row:
                heapq.heappush(max_heap, -num)  # Use negative values to simulate a max-heap
                if len(max_heap) > k:
                    heapq.heappop(max_heap)

        return -max_heap[0]