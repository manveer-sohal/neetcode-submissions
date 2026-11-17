from collections import Counter, deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            
       
        if len(s) == 0:
            return 0
        longest_substring = 0

        freq = Counter() # counter of the biggest letter in the current substring
        canidate = s[0] # current largest letter

        l = 0
        r = 0
        buffer = 0
        while r < len(s):
            char = s[r] # B
            freq[char] += 1 #{A:1,B:2}

            if freq[char] >  freq[canidate]:
                    canidate = char

            buffer = r - l + 1 - freq[canidate] 
            #l=3
            #r=6
            #counter = 5
            #buffer = 2
            #ls = 5                   012345678
            
            while buffer > k:
                
                temp = s[l]
                freq[temp]-=1 #BAB
                l+=1
                # print(char,r-l+1,canidate,buffer , r , l)
                if temp == canidate:
                    canidate =  max(freq, key=freq.get)
                    # print("bazinga",canidate)
                buffer = r - l + 1 - freq[canidate] 
          
            
            longest_substring = max(longest_substring,r-l+1)
            
           
                

            r+=1
        
        return longest_substring



            




    #    AAABABBPPPBBBBB