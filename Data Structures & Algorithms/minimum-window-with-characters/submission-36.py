from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:


        target = Counter(t)
        curr = Counter()

        need = len(target)
        have = 0

        l = 0

        ret = None
        for r in range(len(s)):
            char = s[r]
            curr[char]+=1

            if target[char] == curr[char]:
                have+=1

            
            while need == have:
                temp = s[l]

                if ret is None:
                    ret = s[l:r+1]

                if len(ret) > r-l+1:
                    ret = s[l:r+1]
                
                curr[temp]-=1
                l+=1

                if curr[temp] < target[temp]:
                    have-=1
            

        return "" if ret == None else ret
            

                
                
                




      
