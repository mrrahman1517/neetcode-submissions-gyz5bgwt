class MedianFinder:

    # algorithm maintain a max heap of elements smaller than median
    # min heap of elements larger than median

    def __init__(self):
        # init two heaps
        self.small_max_heap = [] # track elements less than median
        self.large_min_heap = [] # track elements larger than median

    def addNum(self, num: int) -> None:
        # first add to smaller side heap
        heapq.heappush(self.small_max_heap, -num)
        
        # Maintain size balance and order
        if self.small_max_heap and self.large_min_heap and (-self.small_max_heap[0] > self.large_min_heap[0]):
            val = -heapq.heappop(self.small_max_heap)
            heapq.heappush(self.large_min_heap, val)

        if len(self.small_max_heap) > len(self.large_min_heap) + 1:
            val = -heapq.heappop(self.small_max_heap)
            heapq.heappush(self.large_min_heap, val)
        elif len(self.large_min_heap) > len(self.small_max_heap) + 1:
            val = heapq.heappop(self.large_min_heap)
            heapq.heappush(self.small_max_heap, -val)

    def findMedian(self) -> float:
        if len(self.small_max_heap) == len(self.large_min_heap):
            return (-self.small_max_heap[0] + self.large_min_heap[0]) / 2.0
        if len(self.small_max_heap) > len(self.large_min_heap):
            return float(-self.small_max_heap[0])
        return float(self.large_min_heap[0])