class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        



        l = 1
        r = max(piles)
       

        def eatBananas(banans_phr):

            elapsed_hrs=0
            for pile in piles:

                elapsed_hrs += (pile // banans_phr) +  (pile % banans_phr > 0)

           
            if elapsed_hrs <= h:
              
                return True
            else:
                return False
                
       


        while l <= r:
            m = (l + r)//2

            if eatBananas(m): # can eat M banans per hour
                r = m -1
            else: # can't eat M banans per hour
                l = m + 1
            
        return l






        
    # 7 = worked
    # 6
    #     [25,10,23,4], h = 9