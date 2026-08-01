class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

       #Longest consequtive sequence 
       # Condition -> 1 greater than the previouse element
       #O(n)
       #Numberes not in order, just any numbers that are consqequtive 

       #10^9, so it has to be o(n) or less


        numbers = set(nums)

        ret = 0
        for num in numbers:
            if num -1 in numbers:
                continue  
            count = 1
            while num + 1 in numbers:
                count+=1
                num+=1
            
            ret = max(ret,count)
        return ret

    
        
        