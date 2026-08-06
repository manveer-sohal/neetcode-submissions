class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #when array is sorted
        #Binary search
        #Divide and conqure
        # Two pointers
        # In place merge
        #Sliding window

        # Small constraints

        # What two pointers will do here is act like a binary search in finding the target. Moving the pointers inward to meet the target.


        l = 0
        r = len(numbers)-1

        while l < r:
            local_sum = numbers[l] + numbers[r]
         
            if local_sum < target:
                l+=1
            elif local_sum > target:
                r-=1
            else:
                return [l+1,r+1]


        

        return -1
        