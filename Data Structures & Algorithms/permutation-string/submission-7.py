from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # permutation means using while loop with tree


        
        target = Counter(s1)
        curr = Counter()
        n1 = len(s1)


        l = 0
        for r, char in enumerate(s2):
        
            curr[char] +=1
            if r - l + 1 > n1:
                outgoing = s2[l]
                curr[outgoing] -=1
                l+=1

            if r - l + 1  == n1 and target == curr:
                return True
            

    
        return False
