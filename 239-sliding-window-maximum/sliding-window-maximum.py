class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # data structure:
        # maybe we can have a map heap with (value, index)
        # so when we pop out, and we see we have pass the index, we can just keep popping

        max_heap = []
        # do the first sliding window of size k first, can also do it in one loop but easier to understand
        res = []
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i],i))
        res.append(-max_heap[0][0])

        for r in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            while max_heap[0][1] < (r-k+1):
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])

        return res
        