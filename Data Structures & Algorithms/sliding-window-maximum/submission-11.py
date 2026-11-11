from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # queue of highest numbers 

        queue = deque()
        ret = []
        l = 0 


        for r in range(len(nums)):

           
            curr_num = nums[r]
            while queue and nums[queue[-1]] < curr_num:
                queue.pop()
            queue.append(r)

            if r - l + 1 == k:
                while queue[0] < l:
                    queue.popleft()
                index = queue[0]
                value = nums[index]
                ret.append(value)
                l+=1
        
        return ret

            
      


