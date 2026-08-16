"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda x: x.start)
        heap = []
        ret = 0



       
       
        for room in intervals:
        
            # print(room.start,room.end)
            while heap and heap[0] <= room.start:
                heapq.heappop(heap)
                # print(heap)

            heapq.heappush(heap, room.end)    
            ret = max(ret, len(heap))        

        return ret

        