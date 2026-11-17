from collections import Counter, deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            
    
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

            buffer = r - l + 1 - freq[canidate]  #calculate buffer by the current lenght of the string - frequency of the letter
    
            while buffer > k: #the highest frequent letter - the lenght gives a buffer that does not work
                
                temp = s[l]
                freq[temp]-=1 # remove the outgoing letter
                l+=1
              
                if temp == canidate: #if that outgoing letter is the current larget leeter 
                    canidate =  max(freq, key=freq.get) #check if their is a new longest letter
                buffer = r - l + 1 - freq[canidate] # since their is a new canidate, calculate the new buffer
          
            
            longest_substring = max(longest_substring,r-l+1)
            
           
                

            r+=1
        
        return longest_substring



            




    #    AAABABBPPPBBBBB