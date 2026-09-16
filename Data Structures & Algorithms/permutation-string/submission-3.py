class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        target = Counter(s1)
        wnd_size = len(s1)

        current = Counter(s2[:wnd_size-1])


        


        l =0 
        for r in range(wnd_size-1,len(s2)):
            char = s2[r]
            current[char] += 1

            if r-l + 1 == wnd_size:
                if current == target:
                    return True
                
                
                current[s2[l]] -=1
                l+=1
        

        return False



