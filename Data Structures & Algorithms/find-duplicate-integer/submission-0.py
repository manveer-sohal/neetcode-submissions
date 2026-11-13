class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        curr = 0
        while nums[curr] != -1:
            idx = nums[curr]
            nums[curr] = -1

            curr = idx
        
        return curr
