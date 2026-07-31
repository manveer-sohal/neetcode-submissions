from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram, frequency mapping. Need to match conunts 
        #Contains -> set? but this case we do not need look up just matching

        freq_s = Counter(s)
        freq_t = Counter(t)
    
        return True if freq_s == freq_t else False







       

        

        

        
