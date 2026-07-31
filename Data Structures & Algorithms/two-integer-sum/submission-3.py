class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find two nums given a codition
        #index have a constraint
        #1000 can do two for loops
        #But this can be solved with a dict


        target_number = {}

        for idx, num in enumerate(nums):
            if target - num in target_number:
                first_idx = target_number[target-num]
                return[first_idx,idx]
            target_number[num] = idx
        
        return[-1,-1]
        



