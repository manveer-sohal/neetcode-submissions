class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
    #Appears more than once in an array -> Set()

        dupe = set()

        for num in nums:
            if num in dupe:
                return True
            dupe.add(num)
        return False