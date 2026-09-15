class Solution:
    def minWindow(self, s: str, t: str) -> str:
      

        
        

        target = Counter(t)
        target_count = len(target)

        has = Counter()
        has_count = 0

        


        retl , retr = 0 ,len(s) 

        l = 0
        for r in range(len(s)):
            char = s[r]
            has[char]+=1
            if char in target and has[char] == target[char] :
                has_count+=1
            

          
            
            while has_count == target_count:
              
                temp_char = s[l]
                has[temp_char]-=1
               
                if temp_char in target and has[temp_char] < target[temp_char]:
                    has_count-=1
        
                if retr-retl > r-l:
                   
                    retr = r
                    retl = l
                
               

                l+=1
                



        return "" if retr - retl +1 > len(s) else s[retl:retr+1]

