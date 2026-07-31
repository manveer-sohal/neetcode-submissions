import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##10^4, we can sort, heap, binary search, and use dict
        # K most frequent, use a heap or a bucket
    

        freq = Counter(nums)
        heap = []

        
        for num, count in freq.items():
            heapq.heappush(heap,(-count,num))
        
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        
        return ret

