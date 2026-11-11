from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:


        target = Counter(t)
        curr = Counter()

        need = len(target)
        have = 0

        l = 0

        ret =[0,len(s)]
        for r in range(len(s)):
            char = s[r]
            curr[char]+=1

            if target[char] == curr[char]:
                have+=1

            
            while need == have:
                temp = s[l]


                if ret[1]-ret[0] > r-l:
                    ret = [l,r]
                
                curr[temp]-=1
                l+=1

                if curr[temp] < target[temp]:
                    have-=1
            

        return "" if ret[1] == len(s) else s[ret[0]:ret[1]+1]
            

                
                
                




      
