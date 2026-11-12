class Solution:
    def findMin(self, nums: List[int]) -> int:


        
       



        l = 0 
        r = len(nums) - 1

        while l <= r:

            m = (l + r + 1) // 2
            print(nums[l],nums[m],nums[r])

            if nums[l] < nums[m] and nums[m] > nums[r]: #right half
                l = m 
            elif nums[l] > nums[m] and nums[m] < nums[r]: # left half
                r = m 

            else:
                return min(nums[l],nums[m],nums[r])
        

        return nums[l]




