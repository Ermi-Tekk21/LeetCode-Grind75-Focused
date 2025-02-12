class MedianFinder:
    def __init__(self):
        self.maxHeap = [] 
        self.minHeap = [] 

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap) == 0:
            heappush(self.minHeap, num)
        elif self.minHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            heappush(self.maxHeap, -heappop(self.minHeap))

        if len(self.maxHeap) - len(self.minHeap) > 1:
            heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 1:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return -self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()