class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


             #.         []
        #    [1].        [2]         [3]
        # [1,2][1,3].  [2,3]
        

        ret = []
        ret.append([])

        combo = []
        n = len(nums)
        def subsets(index):
            if index == n:
                return
            

            
            for i in range(index,n):
                combo.append(nums[i])
                ret.append(combo.copy())
                subsets(i+1)
                combo.pop()
        

        subsets(0)

        return ret



        