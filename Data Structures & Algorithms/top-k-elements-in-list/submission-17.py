import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##10^4, we can sort, heap, binary search, and use dict
        # K most frequent, use a heap or a bucket
    

        freq = Counter(nums)
        heap = []

        
        for num, count in freq.items():
            #(1, 5) first in heap
            #(3,10) second in heap
            #(7,1) last in heap 
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # ret = []
        # for i in range(k):
        #     #pop out the top k numbers we need
        #     ret.append(heapq.heappop(heap)[1])
        
        return [num for count, num in heap]

